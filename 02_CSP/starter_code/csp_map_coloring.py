"""
Assignment starter: backtracking CSP solver for map colouring.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_csp_map_coloring.py rely on them).

The problem: colour a map of Australia's 7 regions so that no two adjacent
regions share a colour, using only 3 colours.
"""

VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Adjacency list: which regions border which.
# T (Tasmania) is an island -- it has no neighbours,
# so it's unconstrained.

NEIGHBOURS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

DOMAIN = ["Red", "Green", "Blue"]


def is_consistent(assignment, var, value):
    """Return True if assigning `value` to `var` does not conflict
    with any already-assigned neighbour of `var`.
    """

    for neighbour in NEIGHBOURS[var]:
        if neighbour in assignment:
            if assignment[neighbour] == value:
                return False

    return True


def select_unassigned_variable(assignment):
    """Return the first unassigned variable in VARIABLES order.

    Return None if all variables are assigned.
    """

    for variable in VARIABLES:
        if variable not in assignment:
            return variable

    return None


def backtracking_search(variables, domain):
    """Run backtracking search and return a complete, consistent
    assignment, or None if no solution exists.
    """

    def backtrack(assignment):
        # Step 1: Check whether the assignment is complete.
        if len(assignment) == len(variables):
            return assignment.copy()

        # Step 2: Select an unassigned variable.
        var = select_unassigned_variable(assignment)

        # Step 3: Try every value in the domain.
        for value in domain:

            # Step 4: Check whether the value is consistent.
            if is_consistent(assignment, var, value):

                # Tentatively assign the value.
                assignment[var] = value

                # Step 5: Recursively continue the search.
                result = backtrack(assignment)

                # If a solution was found, return it.
                if result is not None:
                    return result

                # Step 6: The choice failed, so undo it.
                del assignment[var]

        # Step 7: No value works for this variable.
        return None

    # Start with an empty assignment.
    return backtrack({})


if __name__ == "__main__":
    solution = backtracking_search(VARIABLES, DOMAIN)

    if solution:
        print("Solution found:")

        for region in VARIABLES:
            print(f"  {region}: {solution[region]}")

    else:
        print("No solution exists with this domain.")