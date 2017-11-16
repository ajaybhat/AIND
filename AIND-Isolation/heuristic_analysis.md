# Heuristics Analysis for Isolation Game agent

### Results
The results of the tournament played with different agents is below:

| Match  |  Opponent   | AB_Improved |  AB_Custom  | AB_Custom_2 | AB_Custom_3 |
|:------:|-------------|:------------:|:-------------:|:-------------:|:----------:|
|      |              | Won , Lost | Won , Lost  | Won , Lost  | Won , Lost |
|   1  |    Random    |   9  ,  1  | 10  ,  0  |   8  ,  2  |  7  ,  3  |
|   2  |    MM_Open   |   6  ,  4  |  7  ,  3  |   6  ,  4  |  6  ,  4  |
|   3  |   MM_Center  |   8  ,  2  |  8  ,  2  |   5  ,  5  | 10  ,  0  |
|   4  |  MM_Improved |   8  ,  2  |  7  ,  3  |   7  ,  3  |  7  ,  3  |
|   5  |    AB_Open   |   5  ,  5  |  5  ,  5  |   4  ,  6  |  5  ,  5  |
|   6  |   AB_Center  |   6  ,   4 |  8  ,  2  |   6  ,  4  |  8  ,  2  |
|   7  |  AB_Improved |   5  ,   5 |  6  ,  4  |   5  ,  5  |  3  ,  7  |
|          **Win Rate:** | |   67.1%    |    72.9%    |    58.6%    |    65.7%        |

### Analysis

#### Heuristic 1
The first heuristic used was the weighted difference between number of player's moves and the opponents moves. A random weight between 0 and 1 was applied to each of the player and opponent's moves. Randomizing weights seemed like a good idea because it would remove any bias than if the weights were arbitrarily assigned. This seemed like the simplest heuristic which would give good results. 

The heuristic gave a winning rate of 72.9%, which is a vast improvement over the "improved" heuristic of the sample player, most likely due to the random weights assigned to the number of moves. The weights act as "penalties" for the number of moves.

#### Heuristic 2
The second heuristic applied was the difference between the number of blank spaces and the player's legal moves. In case the player has more legal moves than blank spaces are available, their score would be lower. A random weight between 0 and 1 was applied to the number of players moves. 

The heuristic gave a winning rate of 58.6%, which is the worst of all the three. Possibly the number of blank spaces doesnt really affect the outcome of the game very much

#### Heuristic 3
The third heuristic applied was a modification of the first. After applying a random weights, the squared difference was taken between the number of  players moves and opponents moves. 

This heuristic gave a winning rate of 65.7%, which is average compared to Heuristic 1, but worse than the "improved" heuristic. It is too complex and not recommended for use.

### Conclusion

Out of the three, Heuristic 1 performed the best.
Some of the reasons for choosing it are:
* The win rate for this heuristic is the highest among all the three with 72.9% 
* The heuristic employs minimal complexity, using random weights on simple difference of the player's and opponent's moves to achieve a proper discriminant on the outcome of the game
* Traversal of the game tree is also deeper in the case of Heuristic 1
