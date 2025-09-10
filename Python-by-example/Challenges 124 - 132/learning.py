# from tkinter import*

# def Call():
#     msg = Label(window, text = "You pressed the button")
#     msg.place(x=30, y = 50)
#     button["bg"] = "blue"
#     button["fg"] = "white"

# window = Tk()
# window.geometry("200x110")
# button = Button(text = "Press me", command = Call)
# button.place(x = 30, y =20, width=120, height=25)
# window.mainloop()

from tkinter import*

def Go():
    msg = Label(window, text= "Hello")
window = Tk()
window.title("Challenge 124")
window.geometry("450x100")

entry_box = Entry(text = "Enter a name")
button = Button(text="Click", command= Go)

window.mainloop()