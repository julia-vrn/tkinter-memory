from tkinter import *
import time
from random import shuffle

global previous_card
previous_card = None
global cards_to_close
cards_to_close = []
global matches
matches = []


class Cell:
    def __init__(self, master, r, c):
        self.image = NONE
        self.r = r
        self.c = c
        self.zaglushka = PhotoImage(file="card.png")
        self.btn = Button(width=100, height=100, image=self.zaglushka, command=self.show_card)
        self.btn.grid(row=r, column=c)
        self.face_up = False

    def set_image(self, image):
        self.image = image

    def show_card(self):
        global previous_card
        global cards_to_close
        global matches
        if len(cards_to_close) != 0:
            cards_to_close[0].hide_card()
            cards_to_close[1].hide_card()
        if len(cards_to_close) > 0:
            for k in range(0, len(cards_to_close)-1):
                cards_to_close[k].hide_card()
                cards_to_close.clear()

        self.btn.config(image=self.image)
        self.btn['command'] = 0

        self.face_up = True

        if previous_card is None:
            previous_card = self
        elif previous_card is not None:
            if previous_card.image != self.image:
                cards_to_close = [self, previous_card]
            elif previous_card.image == self.image:
                matches.append(self)
                matches.append(previous_card)
                if len(matches) == 6:
                    resultlbl = Label(root, text="you won")
                    resultlbl.grid(row=0, column=0)
            previous_card = None

    def hide_card(self):
        self.btn.config(image=self.zaglushka)
        self.btn.config(command=self.show_card)
        self.face_up = False


root = Tk()
blank_card = PhotoImage(file="card.png")

counter_lbl = Label(text="")
counter_lbl.grid(row=0, column=1)

owl = PhotoImage(file="owl.png")
bee = PhotoImage(file="bee.png")
frog = PhotoImage(file="frog.png")

image_list = [owl, owl, bee, bee, frog, frog]
shuffle(image_list)

board = []

rw = 2 #количество рядов в игровом поле
cl = 3 #количество столбцов в игровом поле

for i in range(0, rw):
    for j in range(0, cl):
        board_cell = Cell(root, i+1, j)
        board.append(board_cell)


for i in range(0, len(image_list)):
    board[i].set_image(image_list[i])


for i in range(0, len(board)):
    if board[i].face_up == True:
        board[i].show_card()


root.mainloop()