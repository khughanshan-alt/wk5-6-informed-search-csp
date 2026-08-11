# Week 5-6 Notes

## A* Heuristic

The Manhattan distance heuristic is admissible because movement is restricted to four directions, so the Manhattan distance gives the minimum number of horizontal and vertical moves required to reach the goal while ignoring obstacles. It never overestimates the actual path cost because walls can only make the real path equal to or longer than the Manhattan distance.

## Test Case Design

The six test cases cover different branches of the mind-map rather than repeating the same scenario. The A* tests cover a typical case with obstacles, a boundary case, and an unsolvable case, while the CSP tests cover constraint consistency, an unconstrained boundary case involving Tasmania, and an over-constrained unsolvable case.