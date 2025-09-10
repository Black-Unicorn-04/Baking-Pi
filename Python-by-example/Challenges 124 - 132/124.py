from tkinter import*

window = Tk()
window.geometry("500x200")
window.title("Challenge 124")

label1 = Label(text="Enter your name:")
label1.place(x=30, y = 20)

textbox1 = Entry(text="")
textbox1.place(x=30, y =50, width = 200, height = 40)
# textbox1["justify"] = "center"

window.mainloop()