import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
root = tk.Tk()
root.configure(background='black')
root.title("Meeting Summarizer")

background_image = PhotoImage(file='bgfF.png')

# create a label widget to display the image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def com_as():
   root.destroy()
   import aboutus

def SUT():
    root.destroy()
    import SUT
def SUA():
    root.destroy()
    import SUA
#helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")

heading_font = font.Font(family="Allerta Stencil 400", weight="bold")
menu_font = font.Font(family="Arial",font=50)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

about_menu = tk.Menu(menu_bar,tearoff=0,foreground='purple',font=12)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About",command=com_as)

text_menu = tk.Menu(menu_bar, tearoff=0,foreground='purple',font=12)
menu_bar.add_cascade(label="Summarizer using Text", menu=text_menu)
text_menu.add_command(label="Summarize Text",command=SUT)

audio_menu = tk.Menu(menu_bar, tearoff=0,foreground='purple',font=12)
menu_bar.add_cascade(label="Summarizer using Audio", menu=audio_menu)
audio_menu.add_command(label="Summarize Audio",command=SUA)

about_menu = tk.Menu(menu_bar,tearoff=0,foreground='purple',bg='#F3F0Ee', font=('Arial', 16, 'underline','italic','bold'))
menu_bar.add_cascade(label="GET PRO", menu=about_menu)
about_menu.add_command(label="GET PRO",command=com_as)





# Create an object of tkinter ImageTk


heading_label = tk.Label(root, font=(heading_font,39),bg='black',foreground='white')
#Allerta Stencil 400
heading_label.pack()

heading_label.place(anchor='center',relx=0.5,rely=0.7)
root.geometry("1100x1000")

# create a PhotoImage object from the image file



root.mainloop()