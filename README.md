# Chess-AI
A multi-difficulty chess AI.

The chess GUI was built using the PyGame library. 

The AI was built using the naive 'minimax' algorithm, which works by recursively performing a programmer-defined evaluation function on every move possible, it then elects the move which has the best evaluation. 

The difficulty of the AI can be changed by adjusting the number of moves in advance it takes into account: a depth of 1 will mean the AI simply picks the best move there and then, not taking into account what the best response of the player would be, and the implications of that therefore; a depth of 3, then, will mean that the AI picks the best move, assuming that the player picks the best move, in response to the AI picking the best move.

The run time of the minimax algorithm can be reduced through alpha-beta optimisation, which I have implemented. I should say, however, that, unless you have a PC with more than 16GB of RAM and a decent CPU, a depth of 4 will probably exceed the limit of most people's patience: I found run-time to be an average of about ninety seconds per move - the moves are inordinately better than those of depth 3 however.

You can unhash the code in main.py on ~line 57 to watch the AI play against itself.
You can also unhash the code in minimax/algorithm.py on ~line 55 to visualise the AI's calculations in real time.
