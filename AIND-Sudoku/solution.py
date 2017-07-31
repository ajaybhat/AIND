assignments = []


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    return eliminate_naked_twins_peers(get_naked_twins(values), values)


def eliminate_naked_twins_peers(naked_twins, values):
    '''
    Get the intersection of the set of peers for each naked twin. 
    For each peer that has > 2 choices, eliminate both digits of the twins.
    :param naked_twins: Pair of naked twins 
    :param values(dict): a dictionary of the form {'box_name': '123456789', ...} 
    :return: the values dictionary with the naked twins eliminated from peers.
    '''
    for pair in naked_twins:
        twin1, twin2 = pair
        digit1, digit2 = values[twin1][0], values[twin1][1]
        combined_peers = [peer for peer in peers[twin1] & peers[twin2] if len(values[peer]) > 2]
        for peer in combined_peers:
            values = assign_value(values, peer, values[peer].replace(digit1, ''))
            values = assign_value(values, peer, values[peer].replace(digit2, ''))
    return values


def get_naked_twins(values):
    '''
    Find all values with 2 choices for digits in the grid. 
    Of those, pair off the values that are peers of each other and have same choices
    :param values: 
    :return: 
    '''
    naked_twins_candidates = [box for box in values.keys() if len(values[box]) == 2]
    naked_twins = [[box1, box2] for box1 in naked_twins_candidates
                   for box2 in peers[box1]
                   if values[box1] == values[box2]]
    return naked_twins


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    grid = ['123456789' if value is '.' else value for value in grid]
    return dict(zip(boxes, grid))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)


def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values = assign_value(values, peer, values[peer].replace(digit, ''))
    return values


def only_choice(values):
    for unit in unit_list:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
    return values


def reduce_puzzle(values):
    '''
    Perform elimination, only-choice and Naked twins on the Sudoku grid
    :param values(dict): The sudoku in dictionary form
    :return: values(dict): The sudoku in dictionary form after operations are done
    '''
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(values=grid_values(grid=grid))


rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonal_units = [[row + column for row, column in zip(rows, cols)],
                  [row + column for row, column in zip(rows, cols[::-1])]]
unit_list = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - {s}) for s in boxes)

if __name__ == '__ma2in__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
