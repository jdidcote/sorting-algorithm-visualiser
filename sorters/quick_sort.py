from sorters.base import BaseSorter

from data_model.sort_iteration import SortIter
from utils import non_matching_elements

class QuickSorter(BaseSorter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sort_history = []
        # self.l = self._quick_sort(self.l)
        self._quick_sort(self.l)

    def sort(self):
        for i in self.sort_history:
            yield i

    def _add_to_history(self, l, index, changes):
        self.sort_history.append(SortIter(l, [index], changes))

    def _quick_sort(self, l, idxs=None):
        if len(l) < 2:
            return l

        if idxs is None:
            # idxs = [0 for _ in enumerate(l)]
            idxs = [x for x, _ in enumerate(l)]
            
        pivot = l[0]

        left, right = [], []
        left_idxs, right_idxs = [], []

        # Split into left and right, also track indexes
        for idx, val in enumerate(l):
            self._add_to_history(self.l[:], idxs[idx], [])
            if val < pivot:
                left.append(val)
                left_idxs.append(idxs[idx])
            elif val > pivot:
                right.append(val)
                right_idxs.append(idxs[idx])

        outputs =  self._quick_sort(left, left_idxs) + [pivot] + self._quick_sort(right, right_idxs)
        
        sorted_idxs = left_idxs + [idxs[0]] + right_idxs
        for idx, output in zip(idxs, outputs):
            self.l[idx] = output
        self._add_to_history(self.l[:], None, idxs)

        return outputs