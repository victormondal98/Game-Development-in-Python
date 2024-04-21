import sys
from tkinter import Button, Label
import random
import ctypes
import Config
import sys


class Cell:
    all = []
    cell_count_label_object = None
    cell_count = Config.Cell_count

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=5,
        )
        'Assign Events to the buttons'
        btn.bind('<Button-1>', self.left_click)  # <Button-1> is just the convention of saying 'Left Click'
        btn.bind('<Button-3>', self.right_click)  # <Button-1> is just the convention of saying 'Right Click'
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='darkslategray1',
            fg='black',
            text=f'Cells left: {Cell.cell_count}',
            width=20,
            height=11,
            font=("Courier", 12)
        )
        Cell.cell_count_label_object = lbl

    def left_click(self, event):
        #print(event)
        #print("I am left clicked!")
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If total mines count gets equal to the left_cell_count, the player wins.
            if Cell.cell_count == Config.Mine_size:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You have won the Minesweeper game!', 'Game Over', 0)


        # Cancel the Right and Left click events, if the cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # Return cell object based on x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter = counter + 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mine_length)

            # Replace the count dynamically with newer count everytime you click on a button
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f'Cells left: {Cell.cell_count}')
            # If this was a mine candidate, then configure back the button's original colour
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        # Mark the cells as opened. Use this line as the last line of the method
        self.is_opened = True

    def show_mine(self):
        # A logic to interrupt the game and display the player that he has lost
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    def right_click(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='green'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False
        """
        print(event)
        print("I am right clicked!")"""

    @staticmethod
    def randomize_mines():
        randomly_picked_cells = random.sample(
            Cell.all, Config.Mine_size
        )
        # turn them into mines
        for random_cell in randomly_picked_cells:
            random_cell.is_mine = True

    # Below is the magic method to Represent the object class
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
