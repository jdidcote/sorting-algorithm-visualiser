from typing import List

from data_model.sort_iteration import SortIter
from sorters.base import BaseSorter
from utils import non_matching_elements

class MergeSorter(BaseSorter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.merge_history = []
        self._merge_sort(self.l)

    def sort(self):
        for i in self.merge_history:
            yield i

    def _merge_sort(self, l: List[int], idx: int=0) -> List[int]:
        """Merge sort algorithm

        Args:
            l (List[int]): list
            idx (int, optional): start index of the original (unpartitioned) - used for tracking. Defaults to 0.

        Returns:
            List[int]: sorted list
        """

        if len(l) == 1:
            return l

        # Find the mid-point of the array
        mp = len(l) // 2

        # Split into left and right
        left, right = l[:mp], l[mp:]

        # Track original list indeces for partitions
        orig_idx_left = idx
        orig_idx_right = mp + idx

        # Recursively split list
        left_partition = self._merge_sort(left, orig_idx_left)
        right_partition = self._merge_sort(right, orig_idx_right)

        # Sort left and right partitions
        return self._merge(left_partition, right_partition, orig_idx_left, orig_idx_right)

    def _add_to_history(self, l, index, changes):
        self.merge_history.append(SortIter(l, [index], changes))

    def _merge(
        self,
        left: List[int], 
        right: List[int],
        idx_left: List[int],
        idx_right: List[int]
    ) -> List[int]:
        # Modified code from here https://stackoverflow.com/questions/66895275/python-merge-sort-algorithm
        output = []
        il = 0
        ir = 0
        temp_l = self.l[:]

        while il < len(left) and ir < len(right):
            if left[il] <= right[ir]:
                output.append(left[il])
                self._add_to_history(temp_l, il + idx_left, [])
                il += 1
            else:
                output.append(right[ir])
                self._add_to_history(temp_l, ir + idx_right, [])
                ir += 1
        while il < len(left):  
            output.append(left[il])
            self._add_to_history(temp_l, il + idx_left, [])
            il += 1
        while ir < len(right):
            output.append(right[ir])
            self._add_to_history(temp_l, ir + idx_right, [])
            ir += 1

        # Update the stored list
        self.l[idx_left:(idx_right + len(right))] = output

        # Get the indexes of the original list which have changed
        changes = non_matching_elements(self.l, temp_l)

        self._add_to_history(self.l[:], None, changes)

        return output