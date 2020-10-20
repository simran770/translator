from tkinter import *
from translate import Translator

root = Tk()
root.title("GUI translator")

choice1 = StringVar(root)
choice2 = StringVar(root)

choices = {'english', 'hindi', 'gujarati', 'spanish', 'germany'}

choice1.set('english')
choice2.set('hindi')


def translate():
    translator = Translator(from_choiceg=choice1.get(), to_lang=choice2.get())

    translation = translator.translate(var.get())
    var1.set(translation)


choice1Menu = OptionMenu(root, choice1, *choices)
Label(root, text="Choose a Language").grid(row=0, column=1)
choice1Menu.grid(row=1, column=1)

choice2Menu = OptionMenu(root, choice2, *choices)
Label(root, text="Translated Language").grid(row=0, column=2)
choice2Menu.grid(row=1, column=2)

Label(root, text="Enter text here").grid(row=2, column=0)
var = StringVar()
textbox = Entry(root, textvariable=var).grid(row=2, column=1)

Label(root, text="Output").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(root, textvariable=var1).grid(row=2, column=3)

b = Button(root, text='Translate', command=translate, relief=GROOVE).grid(row=3, column=1, columnspan=3)
mainloop()
