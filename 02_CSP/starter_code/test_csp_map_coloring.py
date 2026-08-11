"""
Tests for csp_map_coloring.py

Run with:
pytest 02_CSP/starter_code/test_csp_map_coloring.py -v

The given example is complete.

The three required test cases cover different categories:
1. Constraint consistency
2. Edge / boundary case
3. Unsolvable / over-constrained case
"""

import pytest

from csp_map_coloring import backtracking_search, is_consistent


def _is_valid_solution(solution, variables, neighbours):
    """Helper: check a solution assigns every variable and breaks no
    adjacency constraint.
    """

    if solution is None:
        return False

    if set(solution.keys()) != set(variables):
        return False

    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution and solution[neighbour] == value:
                return False

    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify.
#
# Category: typical/normal solvable case.
# ---------------------------------------------------------------------

def test_given_example():

    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None

    assert _is_valid_solution(
        solution,
        VARIABLES,
        NEIGHBOURS
    )


# ---------------------------------------------------------------------
# TEST CASE 1
#
# Category: constraint consistency.
# This checks that a variable cannot have the same colour as an
# already-assigned neighbouring variable.
# ---------------------------------------------------------------------

def test_case_1():

    assignment = {
        "NT": "Red"
    }

    # WA borders NT, so WA cannot also be Red.
    assert is_consistent(
        assignment,
        "WA",
        "Red"
    ) is False

    # Green does not conflict with NT.
    assert is_consistent(
        assignment,
        "WA",
        "Green"
    ) is True


# ---------------------------------------------------------------------
# TEST CASE 2
#
# Category: edge / boundary case.
# Tasmania (T) has no neighbours, so it is unconstrained.
# ---------------------------------------------------------------------

def test_case_2():

    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(
        VARIABLES,
        DOMAIN
    )

    assert solution is not None

    # Tasmania must be included in the complete solution.
    assert "T" in solution

    # Tasmania has no neighbouring regions.
    assert NEIGHBOURS["T"] == []

    # Its colour must be one of the available colours.
    assert solution["T"] in DOMAIN


# ---------------------------------------------------------------------
# TEST CASE 3
#
# Category: unsolvable / over-constrained case.
# With only one colour, neighbouring regions cannot be assigned
# different colours, so the Australia map has no solution.
# ---------------------------------------------------------------------

def test_case_3():

    from csp_map_coloring import VARIABLES

    solution = backtracking_search(
        VARIABLES,
        ["Red"]
    )

    assert solution is None


# ---------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    sys.exit(
        pytest.main(
            [__file__, "-v"]
        )
    )