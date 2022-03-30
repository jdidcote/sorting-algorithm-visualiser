from abc import ABC, abstractmethod
from typing import List

from data_model.sort_iteration import SortIter

class BaseSorter(ABC):
    def __init__(self, l: List[int]):
        """Base sorting algorithm which all other sorting classes must inherit

        Args:
            l (List[int]): unsorted list of integers
        """
        self.l_orig = l[:]
        self.reset()

    def __len__(self):
        return len(self.l)

    @property
    def is_sorted(self):
        return all([self.l[i] <= self.l[i + 1] for i in range(len(self) - 1)])

    @abstractmethod
    def sort(self) -> SortIter:
        """Sort the unordered list and save any changes
        """
        pass

    def swap(self, i0: int, i1: int):
        """Swap two array elements and add to swaps history

        Args:
            i0 (int): index of first element
            i1 (int): index of second element
        """
        self.swaps += 1
        self.swap_history.append((i0, i1))
        self.l[i0], self.l[i1] = self.l[i1], self.l[i0]

    def reset(self):
        """Reset the objects state
        """
        self.l = self.l_orig[:]
        self.iterations = 0
        self.swaps = 0
        self.swap_history = []
