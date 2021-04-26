"""
Name: Masud Hussain
Course: CS162
Assignment: 4A
"""


# Initialize the TargetNotFound class that initializes a new message as a parameter
class TargetNotFound(Exception):
    def __init__(self, new_message):
        self.message = new_message

    def __str__(self):
        return self.message


# Binary search function that returns the index of the target variable from the list
def binary_search(a_list, target):
    """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
    first = 0
    last = len(a_list) - 1

    # Initialize a boolean that is set as False by default
    found = False

    # Run the loop while found is false
    if found is False:
        while first <= last:
            middle = (first + last) // 2
            if a_list[middle] == target:
                print(middle)
                found = True
            if a_list[middle] > target:
                last = middle - 1
            else:
                first = middle + 1

    # Raises exception error if there is no occurrence of the target var in the list
    if not found:
        raise TargetNotFound("Target not found")
