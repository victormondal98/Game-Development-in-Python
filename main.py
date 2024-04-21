from tkinter import *
import Config
import Custom_Functions
from Cells import Cell

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{Config.Width}x{Config.Height}')
root.title("Minesweeper Game")
root.resizable(False, False)

# Add frames for different segments of the window, for different task i.e Title, Score Board, Game Play

# Top Frame
Top_Frame = Frame(
    root,
    bg='dodgerblue2',
    width=Config.Width,
    height=Custom_Functions.height_prct(10)
)
Top_Frame.place(x=10, y=10)

# Add the Heading/Title of the game to the Top Frame
Game_Title = Label(
    Top_Frame,
    bg='dodgerblue2',
    fg='Black',
    text='Minesweeper Game',
    font=('Courier', 20)
)
Game_Title.place(x=Custom_Functions.width_prct(35),y=10)

'----------------------------------------------------------------------------------------------------------'
# Left Frame
Left_Frame = Frame(
    root,
    bg='dodgerblue2',
    width=Custom_Functions.width_prct(25),
    height=Custom_Functions.height_prct(90)
)
Left_Frame.place(x=10, y=str(int(Custom_Functions.height_prct(10)) + 20))
'-------------------------------------------------------------------------------------------------------------'
# Centre Frame, Where the actual interactive gameplay happens
Centre_Frame = Frame(
    root,
    bg='purple',
    width=Custom_Functions.width_prct(75),
    height=Custom_Functions.height_prct(90)
)
Centre_Frame.place(x=Custom_Functions.width_prct(25) + 22, y=Custom_Functions.height_prct(10) + 20)
'------------------------------------------Frames End---------------------------------------------------------'

'------------------------------------------Add Cells/Place Buttons--------------------------------------------'
"""
We can manually add the buttons. For the beginners, it is easy to understand the basic first before
heading to something complex.

Below examples shows how we can manually create and place each cell.
If you are going through this step by step, then consider below codes and run for understanding purpose.
As I am developing it here end to end, I will disable this.

We will, use nested for loop to create each cells for our Gameplay screen.
 
# Examples of Manual process
c1 = Cell()
print(c1.cell_btn_object)
c1.create_btn_object(Centre_Frame)
#c1.cell_btn_object.place(x=0,y=0) # Place method is not useful here. We will be using grid method for easy coordinates
c1.cell_btn_object.grid(column=0,row=0)

c2 = Cell()
print(c2.cell_btn_object)
c2.create_btn_object(Centre_Frame)
#c2.cell_btn_object.place(x=0,y=0) # Place method is not useful here. We will be using grid method for easy coordinates
c2.cell_btn_object.grid(column=1,row=0)

"""

# Nested for loop for each cell creation/ Button type properties added with events on clicks.
for x in range(Config.Grid_size):
    for y in range(Config.Grid_size):
        c = Cell(x, y)
        c.create_btn_object(Centre_Frame)
        c.cell_btn_object.grid(column=x, row=y)

'------------------------------Cells Added/Ends----------------------------------------------------'
# Call the Label from the Cell class
Cell.create_cell_count_label(Left_Frame)
Cell.cell_count_label_object.place(x=0, y=0)

# Place the freshly created mines using Cell.randomize_mines method
Cell.randomize_mines()
"""
Below code is used to check, if we have assigned the mines correctly
Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)
"""






# Run the window
root.mainloop()
