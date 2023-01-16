from __future__ import annotations


class Row(list):

    def __init__(self, string: str):
        super().__init__(map(int, string.split()))

    def add(self, row: Row, factor: int = 1) -> None:
        for i in range(len(self)):
            self[i] = (self[i]+row[i]*factor) % 3

    def __iadd__(self, other: Row) -> Row:
        for i in range(len(self)):
            self[i] += other[i]
            self[i] %= 3
        return self

    def __mul__(self, factor: int) -> Row:
        for i in range(len(self)):
            self[i] *= factor
            self[i] %= 3
        return self

    def __str__(self) -> str:
        return ' '.join(map(str, self))


class Matrix(list):

    width: int
    height: int

    def __init__(self, file):
        super().__init__(map(Row, file))
        self.height = len(self)
        self.width = len(self[0])

    def __str__(self) -> str:
        return '\n'.join(map(str, self)) + '\n'

    def swap_rows(self, i: int, j: int) -> None:
        self[i], self[j] = self[j], self[i]

    def swap_cols(self, i: int, j: int) -> None:
        for row in self:
            row[i], row[j] = row[j], row[i]

    def disp(self, message: str, condition: bool) -> None:
        if condition:
            print(message)
            print(self)

    def skf(self, p: bool = False) -> None:
        row, col = 0, 0
        count = 0
        while row < self.height and col < self.width:
            if self[row][col]:
                if self[row][col] == 2:
                    self[row] *= 2
                    self.disp(f"Удвоим строку №{row+1}", p)
                for i in range(self.height):
                    if self[i][col] and i != row:
                        if self[i][col] == self[row][col]:
                            self[i] += self[row] * 2
                            self.disp(f"Прибавим к строке №{i+1} удвоенную строку №{row+1}", p)
                        else:
                            self[i] += self[row]
                            self.disp(f"Прибавим к строке №{i+1} строку №{row+1}", p)
                if row != col:
                    self.swap_cols(row, col)
                    self.disp(f"Поменяем местами столбцы №{row+1} и №{col+1}", p)
                row += 1
                col += 1
            else:
                c = True
                for i in range(row+1, self.height):
                    if self[i][col]:
                        self.swap_rows(row, i)
                        self.disp(f"Поменяем местами строки №{row+1} и №{i+1}", p)
                        c = False
                        break
                if c:
                    col += 1
            count += 1


if __name__ == '__main__':

    M = Matrix(open("matrix.txt", 'r'))

    print(M)
    M.skf(True)
