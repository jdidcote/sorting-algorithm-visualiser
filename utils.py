from typing import List

import random 

def create_unsorted(n_elements: int) -> List[int]:
    """Creates unsorted array of unique integers

    Args:
        n_elements (int): length of array to be created

    Returns:
        List[int]: unsorted list
    """
    unsorted = list(range(n_elements))
    random.shuffle(unsorted)
    return unsorted

def matching_elements(l1: list, l2: list) -> list:
    """Return the elements of l1 and l2 which are in the same position
    """
    return [i for x, i in enumerate(l1) if i == l2[x]]

def non_matching_elements(l1: list, l2: list) -> list:
    """Return the elements of l1 and l2 which are NOT in the same position
    """
    return [x for x, i in enumerate(l1) if i != l2[x]]