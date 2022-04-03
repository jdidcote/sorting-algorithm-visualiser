from dataclasses import dataclass
from typing import List

@dataclass 
class SortIter:
    """Class for storing data from a single iteration of a sorting algorithm
    """
    l: List[int]
    index: List[int]
    changes: List[int]
