from tkinter import *
from rpg import *
from PIL import Image, ImageTk





def updateScreen():
    global SCREEN
    for row in range(ROW):
        for col in range(COL):
            # Opens image
            im = Image.open(str(SCREEN[row][col]) + ".png")
            # Resizes Image
            resized = im.resize((25, 25), Image.ANTIALIAS)
            # Creates Image
            temp_img = ImageTk.PhotoImage(resized)
            # Creates a temporary Label which holds our image, with a border width of 0
            temp = Label(frame_image, image=temp_img, bd=0)
            # Assign image
            temp.image = temp_img
            # Places image on our grid
            temp.grid(row=row, column=col)

# Move Functions:

def move_up(event):
    move(-1, 0)
    updateScreen()

def move_down(event):
    move(1, 0)
    updateScreen()

def move_right(event):
    move(0, 1)
    updateScreen()

def move_left(event):
    move(0, -1)
    updateScreen()

# COLOUR SCHEME
# Window Background Colour
BG = "black"
# Text Colour
text_colour = "white"
# Button Colour
button_colour = "yellow"

# Main window
root = Tk()
root.config(bg=BG)
# The Header for our Game
header = Label(root, text="The Game", bg=BG)
header.config(height = 3)
header.grid(row=0, column=0)
# The Frame which will hold all of our images
frame_image = Frame(root)
frame_image.config(bd=10, bg=BG)
frame_image.grid(row=1, column=0)

load_floor(1)
updateScreen()
# message variable which can be used to update the in game message.
message = StringVar()
message.set("This message will constantly update while the game progresses.")
# Creating our message which will be updated
message_label = Message(root, textvariable=message, bg=BG, width=400, justify=CENTER)
message_label.grid(row=2, column=0)

# Button Frame
frame_button = Frame(root)
frame_button.config(bd=10, bg=BG, width=520)
item_button = Button(frame_button, text="Items", width=30, padx=0)
item_button.grid(row=0, column=0)
space_holder_1 = Label(frame_button, width=15, bg=BG)
space_holder_1.grid(row=0, column=1)
menu_button = Button(frame_button, text = "Menu", width =30, padx=0)
menu_button.grid(row=0,column=2)
space_holder_2 = Label(frame_button, width=15, bg = BG)
space_holder_2.grid(row=0, column=3)
password_button = Button(frame_button, text="Passwords", width=30, padx=0)
password_button.grid(row=0, column=4)
frame_button.grid(row=3, column=0)

root.bind("<Left>", move_left)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Right>", move_right)

if __name__ == "__main__":
    root.mainloop()



