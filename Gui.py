from tkinter import *
from Board import Board

class Gui():

    def __init__(self):
        self.board = Board()

        self.counter = 1

        self.root = Tk()
        self.root.title("Boter_Kaas_en_Eieren")

        self.boardFrame = Frame(self.root, width=1280, height=800)
        self.boardFrame.grid(row= 0, column = 0)

        self.messageFrame = Frame(self.root)
        self.messageFrame.grid(row=0, column= 1)

        self.inputFrame = Frame(self.root)
        self.inputFrame.grid(row= 0, column=2)

        self.messageLog = Text(self.messageFrame,height=20)
        self.messageLog.grid()

        #input values#
        self.xInputField = Entry(self.inputFrame)
        self.xInputField.grid(row=1, column=0)

        self.yInputField = Entry(self.inputFrame)
        self.yInputField.grid(row=3, column=0)

        self.submitButton = Button(self.inputFrame, text="submit", command=self.submitValues)
        self.submitButton.grid(row=4, column=0)

        #input labels
        self.xLabel = Label(self.inputFrame, text= "row")
        self.yLabel = Label(self.inputFrame, text="column")

        self.xLabel.grid(row=0, column =0)
        self.yLabel.grid(row=2, column=0)

        for i in range(0, len(self.board.getBoard())):
            for j in range(0, len(self.board.getBoard())):
                cell = self.board.getBoard()[i][j]
                label = Label(self.boardFrame, text=cell.getValue(), font=("Courier", 32))
                label.grid(row=i, column=j, sticky= "nsew", padx=50, pady= 50)


    def main(self):
        self.root.mainloop()

    def getCoordinates(self):
        print(self.board.getBoard())

    def getBoardFrame(self):
        return self.boardFrame

    def getLabelText(self, row, column):
        label = self.getLabel(row, column)
        labelText = label['text']
        return labelText

    def getLabel(self, row, column):
        label = self.boardFrame.grid_slaves(row, column)[0]
        return label

    def insertValuesInBoard(self, row, column, value):
        label = self.getLabel(row, column)
        cell =self.board.getBoard()[row][column]

        #alter the label text
        label.configure(text= value)

        #set value of cell
        cell.setCellValue(value)

    def submitValues(self):
        xCoordinate = self.xInputField.get()
        yCoordinate = self.yInputField.get()

        board = self.board.getBoard()

        cell = board[int(xCoordinate)][int(yCoordinate)]

        winresult = self.board.determineWin(board, 0, 0, 0, [])
        print(winresult)
        if cell.getValue() != ".":
            self.messageLog.insert(INSERT, 'coordinate already has a value. Enter empty coordinate \n')
        else:

            if xCoordinate == "" and yCoordinate == "":
                self.messageLog.insert(INSERT, 'fill in both x and y coordinates \n')
            elif xCoordinate == "":
                self.messageLog.insert(INSERT, 'fill in x-oordinate \n')

            elif yCoordinate == "":
                self.messageLog.insert(INSERT, 'fill in y-coordinate \n')

            else:

                if self.counter % 2 == 0:
                    value = "0"

                else:
                    value = "X"


                self.insertValuesInBoard(int(xCoordinate), int(yCoordinate), value)
                self.messageLog.insert(INSERT, value + " inserted at position: " +str(xCoordinate) + " " + str(yCoordinate) +' \n')

                self.messageLog.insert(INSERT, "counter: " +str(self.counter) + "\n")
                self.counter +=1



g = Gui()
g.main()
