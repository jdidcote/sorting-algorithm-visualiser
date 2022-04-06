import unittest
from collections import deque

from sorters.base import BaseSorter
from sorters.bubble_sort import BubbleSorter
from sorters.merge_sort import MergeSorter
from sorters.quick_sort import QuickSorter
from sorters.selection_sort import SelectionSorter
from utils import create_unsorted


class TestSorters(unittest.TestCase):

    def setUp(self):
        self.unsorted = create_unsorted(100)
        self.sorted = sorted(self.unsorted)

    @staticmethod
    def exhaust(generator):
        deque(generator, maxlen=0)

    def generic_sorter(self, Sorter: BaseSorter):
        sorter = Sorter(self.unsorted)
        self.exhaust(sorter.sort())
        self.assertEqual(
            sorter.l,
            self.sorted
        )

    def test_bubble_sort(self):
        self.generic_sorter(BubbleSorter)

    def test_merge_sort(self):
        self.generic_sorter(MergeSorter)

    def test_quick_sort(self):
        self.generic_sorter(QuickSorter)

    def test_selection_sort(self):
        self.generic_sorter(SelectionSorter)


if __name__ == '__main__':
    unittest.main()