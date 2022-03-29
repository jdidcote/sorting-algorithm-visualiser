from sorters.base import BaseSorter

class BubbleSorter(BaseSorter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def step(self):
        if not self.is_sorted:
            for i in range(len(self) - 1):
                if self.l[i] > self.l[i + 1]:
                    self.l[i], self.l[i + 1] = self.l[i + 1], self.l[i]
                    return i, i + 1