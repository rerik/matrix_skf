from __future__ import annotations


class Row(list):

    def __init__(self, string: str):
        super().__init__(map(int, string.split()))

    def add(self, row: Row, factor: int = 1) -> None:
        for i in range(len(self)):
            self[i] = (self[i]+row[i]*factor) % 3

    def multiply(self, factor: int = 2) -> None:
        self.add(self, factor-1)

    def display(self) -> str:
        return ' '.join(str(self)[1:-1].split(', '))


class Matrix(list):

    width: int
    height: int

    def __init__(self, file):
        super().__init__(map(Row, file))
        self.height = len(self)
        self.width = len(self[0])

    def __repr__(self) -> str:
        ans = []
        for row in self:
            ans.append(row.display())
        return '\n'.join(ans)+'\n'

    def replace_rows(self, i: int, j: int) -> None:
        self[i], self[j] = self[j], self[i]

    def replace_cols(self, i: int, j: int) -> None:
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
                    self[row].multiply()
                    self.disp("Удвоим строку №"+str(row+1), p)
                for i in range(self.height):
                    if self[i][col] and i != row:
                        if self[i][col] == self[row][col]:
                            self[i].add(self[row], 2)
                            self.disp("Прибавим к строке №"+str(i+1)+" удвоенную строку №"+str(row+1), p)
                        else:
                            self[i].add(self[row])
                            self.disp("Прибавим к строке №"+str(i+1)+" строку №"+str(row+1), p)
                if row != col:
                    self.replace_cols(row, col)
                    self.disp("Поменяем местами столбцы №"+str(row+1)+" и №"+str(col+1), p)
                row += 1
                col += 1
            else:
                c = True
                for i in range(row+1, self.height):
                    if self[i][col]:
                        self.replace_rows(row, i)
                        self.disp("Поменяем местами строки №"+str(row+1)+" и №"+str(i+1), p)
                        c = False
                        break
                if c:
                    col += 1
            count += 1


if __name__ == '__main__':

    M = Matrix(open("matrix.txt", 'r'))

    print(M)
    M.skf(True)
