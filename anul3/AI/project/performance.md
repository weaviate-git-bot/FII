### Implemented sorted moves by rating (board evaluation is still with stockfish depth=1)
Also, I have LRU caching for calculating best moves

Finding best opening move, at depth:
- 0: Found best move d2d4 (score: 28) in 0.0564 seconds.
- 1: Found best move d2d4 (score: 28) in 0.0484 seconds.
- 2: Found best move e2e4 (score: 17) in 0.8622 seconds.
- 3: Found best move d2d4 (score: 28) in 3.5205 seconds.
- 4: Found best move d2d4 (score: 20) in 34.2336 seconds.
- 5: Found best move e2e4 (score: 32) in 176.3798 seconds. (to be fair, it was 489.0074 first time it ran, but had a bug, first time might be higher)
- 6: Found best move e2e4 (score: 70) in 1374.2085 seconds.

This means around 500 Nodes/second (stockfish has 1.2M Nodes/second)


### Rewriten engine
Added: mate prunning, added quiessence search, added custom evaluation