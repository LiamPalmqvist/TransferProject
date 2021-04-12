from tkinter import *
from tkinter.ttk import *
import DatabaseHandler


class sqliteWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        window = Frame(self)

        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining config within the master window
        Tk.configure(self, bg='ivory2')
        Tk.title(self, "Show Seats GUI")
        Tk.option_add(self, '*Font', 'helvetica 14')
        Tk.option_add(self, '*Background', 'ivory2')
        Tk.geometry(self, '800x700+600+300')
        # End of defining within master window

        seats = DatabaseHandler.getSeats("All")
        for i in seats:
            for n in i:
                print(n)

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tabControl.add(tab2, text='Tab 2')
        tabControl.pack(expand=1, fill='both')

        frame1 = Frame(self)
        frame1.pack()

        button = Button(self)
        button.config(text="Howdy")
        button.pack()


def main():
    app = sqliteWindow()
    app.mainloop()

main()