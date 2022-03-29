from abc import ABC, abstractmethod
from typing import List

class BaseSorter(ABC):
    def __init__(self, l: List[int]):
        """Base sorting algorithm which all other sorting classes must inherit

        Args:
            l (List[int]): unsorted list of integers
        """
        self.l_orig = l
        self.reset()

    def __len__(self):
        return len(self.l)

    @property
    def is_sorted(self):
        return all([self.l[i] <= self.l[i + 1] for i in range(len(self) - 1)])

    @abstractmethod
    def step(self):
        """Move forward one iteration in the sorting algorithm and returns
           the indices of the changed values.
        """
        pass

    def update(self):
        """Update iterations
        """
        self.iterations += 1

    def reset(self):
        """Reset the objects state
        """
        self.l = self.l_orig
        self.iterations = 0
        
