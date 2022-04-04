from sorters.base import BaseSorter

from data_model.sort_iteration import SortIter

class SelectionSorter(BaseSorter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sort(self):
        size = len(self.l)
        for i in range(size):
            swaps = []
            min_idx = i
            for j in range(i + 1, size):
                if self.l[j] < self.l[min_idx]:
                    yield SortIter(self.l, [j], swaps)
                    min_idx = j
            self.swap(i, min_idx)
            swaps = [i, min_idx]
            yield SortIter(self.l, [i], swaps)