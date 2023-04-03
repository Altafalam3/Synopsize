import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

root = tk.Tk()
def SUT():
   root.destroy()
   import SUT
def SUA():
        root.destroy()
        import SUA
def extra():
       root.destroy()
       import extra

root.configure(background='#242124')
root.title("About Us")
root.geometry("1000x600")
background_image = PhotoImage(file="bg for python.png")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
main_page= tk.Menu(menu_bar, tearoff=0,foreground='purple',font=12)
menu_bar.add_cascade(label="Index", menu=main_page)
main_page.add_command(label="Index",command=extra)
text_menu = tk.Menu(menu_bar, tearoff=0,foreground='purple',font=12)
menu_bar.add_cascade(label="Summarizer using Text", menu=text_menu)
text_menu.add_command(label="Summarize Text",command=SUT)

audio_menu = tk.Menu(menu_bar, tearoff=0,foreground='purple',font=12)
menu_bar.add_cascade(label="Summarizer using Audio", menu=audio_menu)
audio_menu.add_command(label="Summarize Audio",command=SUA)

# create a label widget to display the image
background_label = Label(root, image=background_image,bg='grey')
background_label.place(x=0, y=0, relwidth=1, relheight=1)
ack = tk.Label(root, text="We would like to acknowledge and thank all of the contributors who helped make this app possible.\nContributors:\n\n ABHIGYAN BAFNA--01\n\n ALTAF ALAM--04\n\n AMISHA SHAHI--07\n\nSARAH KHAN--54\n",font = ("Arial", 17),bg='black',fg='#C7B4F7')
ack.pack()
ack.place(relx=0.001,rely=0.05)





root.mainloop()