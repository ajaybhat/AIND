# Heuristics Analysis for Isolation Game agent

### Heuristics
#### Heuristic 1
The first heuristic used was the difference between number of player's moves and the opponents moves. This seemed like the simplest heuristic which would give good results. This gave a decent performance in the tournament

#### Heuristic 2
The second heuristic applied was a weighted version of the first. A random weight between 0 and 1 was applied to the number of players moves and opponents moves. This heuristic performed the best out of all three

#### Heuristic 3
The third heuristic applied was a modification of the second. After applying a random weight, the centered deviation was taken for the number of  players moves and opponents moves. This heuristic performed poorly compared to the others.

### Results
The results of the tournament played with different agents is below:

 | Match  |  Opponent   | AB_Improved ||  AB_Custom  || AB_Custom_2 || AB_Custom_3 ||
 | :-------: |-------------|:-------------:||:-------------:||:-------------:||:----------:||
 |       |              | Won  | Lost  | Won | Lost  | Won | Lost  | Won | Lost |
 |   1  |    Random    |  7  |   3  | 10  |   0  |  7  |   3  |  7  |   3  |
|   2  |    MM_Open   |  8  |   2  |  5  |   5  |  6  |   4  |  5  |   5  |
|   3  |   MM_Center  |  7  |   3  |  8  |   2  |  6  |   4  |  8  |   2  |
|   4  |  MM_Improved |  6  |   4  |  8  |   2  |  8  |   2  |  8  |   2  |
|   5  |    AB_Open   |  5  |   5  |  6  |   4  |  6  |   4  |  6  |   4  |
|   6  |   AB_Center  |  7  |   3  |  5  |   5  |  6  |   4  |  8  |   2  |
|   7  |  AB_Improved |  4  |   6  |  5  |   5  |  4  |   6  |  7  |   3  |
|          ** Win Rate:**  ||   62.9%  ||      67.1%    ||    61.4%   ||     70.0%    ||

