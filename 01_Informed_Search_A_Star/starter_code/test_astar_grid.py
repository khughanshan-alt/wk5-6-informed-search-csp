"""
Tests for astar_grid.py

Run with:
pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v

The given example is complete and is used as a template.

The three required test cases cover different categories:
1. Typical case with obstacles
2. Edge/boundary case
3. Unsolvable case
"""

import pytest

from astar_grid import astar, heuristic, neighbours, find_cell


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify.
# Category: typical/normal small case
# ---------------------------------------------------------------------

def test_given_example():
    grid = [
        "S..",
        "...",
        "..G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal

    # Shortest possible Manhattan path on an open 3x3 grid is 4 moves.
    assert cost == 4


# ---------------------------------------------------------------------
# TEST CASE 1
# Category: Structure -> obstacles / detour
# This tests whether A* can find the shortest path when walls force
# the algorithm to take a different route.
# ---------------------------------------------------------------------

def test_case_1():
    grid = [
        "S#.",
        ".#.",
        "..G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal

    # The walls force the path:
    # (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2)
    assert cost == 4


# ---------------------------------------------------------------------
# TEST CASE 2
# Category: Edge / boundary case
# This tests a path along the top boundary of the grid, checking that
# boundary cells are handled correctly.
# ---------------------------------------------------------------------

def test_case_2():
    grid = [
        "S.G",
        "...",
        "...",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal

    # S is at (0,0) and G is at (0,2).
    # The shortest path requires 2 moves.
    assert cost == 2


# ---------------------------------------------------------------------
# TEST CASE 3
# Category: Unsolvable case
# This tests whether A* correctly reports that no path exists when
# the start and goal are completely separated by walls.
# ---------------------------------------------------------------------

def test_case_3():
    grid = [
        "S#G",
        "###",
        "...",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


# ---------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))