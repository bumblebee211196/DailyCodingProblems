import os
import time


class GameOfLife:
    def __init__(self, cells, n):
        self.cells = cells
        self.display()
        for _ in range(n):
            self.next_gen()
            self.display()

    def get_live_neighbours_count(self, x, y):
        count = 0
        for r, c in self.cells:
            if abs(r - x) > 1 or abs(c - y) > 1 or (x == r and y == c):
                continue
            count += 1
        return count

    def get_neighbours(self, x, y):
        return set(
            [
                (x, y + 1),
                (x, y - 1),
                (x + 1, y),
                (x - 1, y),
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1),
            ]
        )

    def next_gen(self):
        new_cells = set()
        for i, j in self.cells:
            neighbours = self.get_live_neighbours_count(i, j)
            if 2 <= neighbours <= 3:
                new_cells.add((i, j))
        surrouding_cells = set()
        for i, j in self.cells:
            surrouding_cells = surrouding_cells.union(self.get_neighbours(i, j))
            surrouding_cells = surrouding_cells - self.cells
        for i, j in surrouding_cells:
            neighbours = self.get_live_neighbours_count(i, j)
            if neighbours == 3:
                new_cells.add((i, j))
        self.cells = new_cells

    def display(self):
        top = min(self.cells, key=lambda cells: cells[0])[0]
        bottom = max(self.cells, key=lambda cells: cells[0])[0]
        left = min(self.cells, key=lambda cells: cells[1])[1]
        right = max(self.cells, key=lambda cells: cells[1])[1]
        os.system("cls")
        print("-" * 50)
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if (i, j) in self.cells:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("-" * 50)
        time.sleep(1)


GameOfLife(
    {
        (0, 0),
        (1, 0),
        (1, 1),
        (2, 5),
        (2, 6),
        (3, 9),
        (4, 8),
        (10, 21),
        (11, 13),
        (12, 13),
        (12, 14),
        (13, 14),
        (13, 15),
        (11, 12),
        (21, 11),
        (19, 21),
    },
    10,
)
