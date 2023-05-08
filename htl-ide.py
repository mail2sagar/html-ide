from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

window = Tk()

window.title("HTML IDE")

window.minsize(650,650)
window.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))

save_img = ImageTk.PhotoImage(Image.open("save.png"))

exit_img = ImageTk.PhotoImage(Image.open("exit.png"))


label_file_name = Label(window,text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(window)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text_msg = Text(window,height=35,width=80)
my_text_msg.place(relx=0.5,rely=0.5,anchor=CENTER)

my_text_msg.config(background="ivory4")

open_btn = Button(window,image=open_img,text="Open")
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

save_btn = Button(window,image=save_img,text="Save")
save_btn.place(relx=0.11,rely=0.03,anchor=CENTER)

exit_btn = Button(window,image=exit_img,text="Exit")
exit_btn.place(relx=0.17,rely=0.03,anchor=CENTER)

window.mainloop()