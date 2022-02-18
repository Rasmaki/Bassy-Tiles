import random

#Todo: Add function for json level import/export
class LevelGenerator:
    def __init__(self, columns, length):
        self.columns = columns
        self.length = length
        self.content = [[0 for x in range(self.columns)] for y in range(self.length)]
        self.max_tile_per_row = self.columns / 2

    @staticmethod
    #ToDo: Add an exclude vales option
    def next_cycle(columns, max_amount, force_max):
        row = []
        amount = 0
        if force_max:
            amount = max_amount
        else:
            amount = random.randint(1, max_amount)

        for i in range(columns):
            row.append(0)

        tile_indices = random.sample(range(columns), amount)
        for i in tile_indices:
            row[i] = 1

        return row
