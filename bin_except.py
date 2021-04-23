"""
project-4a
Modify the binary search function from the exploration so that,
instead of returning -1 when the target value is not in
the list, raises a TargetNotFound exception

(you'll need to define this exception class).

Otherwise it should function normally.

Name this function bin_except.
"""


def linear_search(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, returns -1, indicating the target value isn't in the list
    """
    # enumerate lets you iterate through both the elements of the list and their indices
    for index, el in enumerate(a_list):
        if el == target:
            return index
    return -1
