from tkinter import *
from tkinter.ttk import *
import DatabaseHandler


class sqliteWindow(Tk):

    @staticmethod
    def seats(frame, showID):
        labelLen = [2, 10, 13, 2, 2, 4, 13, 24]
        seatsList = DatabaseHandler.getSeats(showID, True)
        names = ["Booking ID", "First Name", "Last Name", "Seat Type", "Show ID", "Seat Booked", "Phone Number",
                 "E-mail"]

        for i in range(8):
            wordLabel = Label(frame)
            wordLabel.config(text=names[i], width=len(names[i]))
            wordLabel.grid(row=0, column=i, sticky='w')

        blankLabel = Label(frame)
        blankLabel.config(text="")
        blankLabel.grid(row=1, column=0)

        for i in range(len(seatsList)):
            for f in range(8):
                newText = Label(frame)
                newText.config(text=seatsList[i][f], width=labelLen[f])
                newText.grid(row=i+2, column=f, sticky='w')

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
        Tk.geometry(self, '1100x700+600+300')
        # End of defining within master window

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tab3 = Frame(tabControl)
        tabControl.add(tab1, text='Show 1')
        tabControl.add(tab2, text='Show 2')
        tabControl.add(tab3, text='Show 3')
        tabControl.pack(expand=1, fill='both')

        frame1 = Frame(tab1)
        frame1.pack()

        frame2 = Frame(tab2)
        frame2.pack()

        frame3 = Frame(tab3)
        frame3.pack()

        ### PAGE 1

        page1 = Frame(frame1)
        page1.pack(expand=True)
        button = Button(page1)
        button.config(text="Howdy")
        self.seats(page1, '0')

        ### END OF PAGE 1

        ### PAGE 2

        page2 = Frame(frame2)
        page2.pack(expand=True)
        self.seats(page2, '1')

        ### END OF PAGE 2

        ### PAGE 3

        page3 = Frame(frame3)
        page3.pack(expand=True)
        self.seats(page3, '2')

        ### END OF PAGE 3


def main():
    app = sqliteWindow()
    app.mainloop()
