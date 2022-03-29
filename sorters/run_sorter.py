from sorters.base import BaseSorter

def run_sorter(sorter: BaseSorter):
    while not sorter.is_sorted:
        sorter.step()
        sorter.update()
        print(sorter.l)