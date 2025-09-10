# from tkinter import*

# import random

# window = Tk()
# window.title("Roll a dice")
# window.geometry("100x120")

# button1 = Button(text="Roll", command= slice)
# button1.place(x=30, y = 70, width = 30, height =25)

# answer = Message(text ="")
# answer.place(x=40, y=70, width=30, height =25)

# window.mainloop()


from tkinter import *
import random

def roll_dice():
    result = random.randint(1, 6)
    answer.config(text=str(result))

window = Tk()
window.title("Roll a dice")
window.geometry("150x120")

button1 = Button(window, text="Roll", command=roll_dice)
button1.place(x=50, y=70, width=50, height=25)

answer = Label(window, text="")
answer.place(x=65, y=30, width=20, height=25)

window.mainloop()