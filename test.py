from tkinter import *


class GuiView:
    def __init__(self, master):
        master.configure(bg='ivory2')
        master.title("Password Generator")
        master.option_add('*Font', 'Georgia 12')
        master.option_add('*Background', 'ivory2')
        master.option_add('*Label.Font', 'helvetica 14')
        master.geometry('800x700+600+300')

        alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

        self.radioSelect = IntVar(master)
        for i in range(10):
            for f in range(20):
                newButton = Radiobutton(master)
                newButton.config(text=(alph[i], f + 1), variable=self.radioSelect, value=(i, f))
                newButton.grid(row=i, column=f)


if __name__ == '__main__':
    window = Tk()
    app = GuiView(window)
    window.mainloop()
