## Area_Optimization using Memory State like Recurrent Neural Networks


> This program uses a statefull(Memory) approach for estimating location in space. This is done by carrying information about each unique 2D location throughout the entire programming sequence. This enables visual evaluation of placement and ensures that one can see how "free area" changes with the addition of new individual features............. 

> The concept behind using such an architecture is to mimic a stateful long-term memory Elman/LSTM architecture. 
- The algorithm first uses given parameters to estimate the best placement architecture to maximize used space.

- The algorithm then uses the optimized placement to start feature placement at the edges of the space.
- The eventual output would be a dense-packed 2D placement within the grid specified earlier by the optimization algorithm.


* Note that this programming algorithm is still in development mode *
