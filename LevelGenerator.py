import random


class Levelgenerator():
    def __init__(self, columns, length):
        self.columns = columns
        self.length = length
        self.content = [[0 for x in range(self.columns)] for y in range(self.length)]
        self.max_tile_per_row = self.columns / 2

    def next_cycle(self, columns, max_amount, force_max):
        row = []
        amount = 0
        if force_max:
            amount = max_amount
        else:
            amount = random.randint(1, max_amount)

        tile_indices = random.sample(range(columns), 10)

        for i in range(columns):
            row.append(0)

        for i in tile_indices:
            row[i] = 1
            print('put tiles on position:')
            print(i)

        return row
