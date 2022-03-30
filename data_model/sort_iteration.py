from dataclasses import dataclass
from typing import List

@dataclass 
class SortIter:
    """Class for storing data from iterations of sorting algorithm
    """
    l: List[int]
    index: int
    swaps: List[int]
