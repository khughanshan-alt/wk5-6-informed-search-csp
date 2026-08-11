"""
Assignment starter: A* search on a grid.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_astar_grid.py rely on them).

Grid legend:
'S' = start
'G' = goal
'#' = wall (cannot be entered)
'.' = free cell

Run this file directly to see your solver in action:
python astar_grid.py
"""

import heapq


# The assignment grid. Do not edit this -- your solver must work on this
# AND on any other valid grid (the test file uses different grids too).

ASSIGNMENT_GRID = [
    "S.......",
    ".#..#.#.",
    ".#....#.",
    ".###.##.",
    "...#....",
    "##.#.##.",
    ".....#..",
    ".##...G.",
]


ROWS = len(ASSIGNMENT_GRID)
COLS = len(ASSIGNMENT_GRID[0])


def find_cell(grid, symbol):
    """Return the (row, col) of `symbol` in `grid`. Already implemented."""
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == symbol:
                return (r, c)

    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(grid, r, c):
    """Return True if (r, c) is inside the grid and not a wall.

    Already implemented -- use this inside your neighbours() function.
    """
    rows, cols = len(grid), len(grid[0])

    if not (0 <= r < rows and 0 <= c < cols):
        return False

    return grid[r][c] != "#"


def neighbours(grid, node):
    """TODO: yield the valid 4-directional neighbours of `node` in `grid`.

    `node` is a (row, col) tuple. A neighbour is valid if is_walkable()
    returns True for it. Use up/down/left/right moves only (no diagonals).
    """
    r, c = node

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """TODO: return the Manhattan distance between `node` and `goal`.

    node and goal are (row, col) tuples.
    Manhattan distance = |row1 - row2| + |col1 - col2|.
    This must be admissible for 4-directional grid movement -- explain in
    your submission notes why Manhattan distance satisfies this.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def reconstruct_path(came_from, current):
    """Rebuild the path from start to `current` using the came_from map.

    Already implemented.
    """
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path


def astar(grid, start, goal):
    """TODO: implement the A* algorithm.

    Return a tuple: (path, cost)
      - path: list of (row, col) tuples from start to goal, inclusive.
              Return None if no path exists.
      - cost: total path cost (int). Return float('inf') if no path exists.

    Follow the pseudocode in ../guide.md section 4:
      1. Use a heapq-based priority queue keyed on f(n) = g(n) + h(n).
      2. Track g_score for every discovered node.
      3. Track came_from so you can reconstruct the path.
      4. Track a closed set of fully-expanded nodes.
      5. Stop as soon as you POP the goal node from the open list
         (not merely when you first see it as a neighbour).

    Tie-break tip: pushing tuples like (f, -g, row, col, node) onto the
    heap gives you a deterministic tie-break (prefer larger g) -- see the
    worked example solution for this pattern if you get stuck.
    """

    # Priority queue.
    # Each item is:
    # (f_score, -g_score, row, col, node)
    open_list = []

    # Cost from start to each discovered node.
    g_score = {
        start: 0
    }

    # Used to reconstruct the final path.
    came_from = {}

    # Nodes that have already been fully expanded.
    closed = set()

    # Initial node.
    start_f = heuristic(start, goal)

    heapq.heappush(
        open_list,
        (
            start_f,
            0,
            start[0],
            start[1],
            start
        )
    )

    while open_list:

        # Get the node with the lowest f-score.
        f_score, neg_g, row, col, current = heapq.heappop(open_list)

        # Ignore nodes that were already fully expanded.
        if current in closed:
            continue

        # Important: stop when the goal is POPPED from the queue.
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, g_score[current]

        # Mark current as fully expanded.
        closed.add(current)

        # Check all valid neighbouring cells.
        for neighbour in neighbours(grid, current):

            # Ignore already-expanded nodes.
            if neighbour in closed:
                continue

            # Every movement costs 1.
            tentative_g = g_score[current] + 1

            # If this is a better route to the neighbour...
            if tentative_g < g_score.get(neighbour, float("inf")):

                # Remember how we reached this neighbour.
                came_from[neighbour] = current

                # Store its improved cost.
                g_score[neighbour] = tentative_g

                # Calculate f(n) = g(n) + h(n).
                neighbour_f = (
                    tentative_g
                    + heuristic(neighbour, goal)
                )

                # Add the neighbour to the priority queue.
                heapq.heappush(
                    open_list,
                    (
                        neighbour_f,
                        -tentative_g,
                        neighbour[0],
                        neighbour[1],
                        neighbour
                    )
                )

    # No path was found.
    return None, float("inf")


if __name__ == "__main__":

    start = find_cell(ASSIGNMENT_GRID, "S")
    goal = find_cell(ASSIGNMENT_GRID, "G")

    print(f"Start: {start}, Goal: {goal}")

    path, cost = astar(
        ASSIGNMENT_GRID,
        start,
        goal
    )

    if path:
        print(f"Path found (cost={cost}):")

        print(
            " -> ".join(
                str(p) for p in path
            )
        )

    else:
        print("No path exists.")