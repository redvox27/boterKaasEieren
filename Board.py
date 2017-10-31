import copy
from Cell import Cell

class Board():
    def __init__(self):
        w, h = 3, 3
        self.board = [[Cell() for x in range(w)] for y in range(h)]

    def getBoard(self):
        return self.board

    def setValue(self, row, column, value):
        board = self.getBoard()
        board[row][column].setCellValue(value)

    def determineWin(self, board, x, y, count, valueList):

        if count == 3 or len(valueList) == 3:
            #print(valueList)
            return valueList

        else:
            tempList = copy.copy(valueList)
            cell = board[x][y]
            value = cell.getValue()

            if value == "X" or value == "Y":
                tempList.append(value)

            #vertical

            self.determineWin(board, x+1, y, count+1,tempList)

            #horizontal

            self.determineWin(board, x, y+1, count+1,tempList)

            #diagonal
            self.determineWin(board, x+1, y+1, count+1,tempList)



b = Board()
b.setValue(0, 0, "X")
b.setValue(0, 1, "X")
b.setValue(0, 2, "X")
print(b.determineWin(b.getBoard(), 0, 0, 0, []))