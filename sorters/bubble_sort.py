from sorters.base import BaseSorter

from data_model.sort_iteration import SortIter

class BubbleSorter(BaseSorter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def sort(self):
        while not self.is_sorted:
            for i in range(len(self) - 1):
                swaps = []
                self.iterations += 1
                if self.l[i] > self.l[i + 1]:
                    self.swap(i, i + 1)
                    swaps = [i, i + 1]
                yield SortIter(self.l, i, swaps)