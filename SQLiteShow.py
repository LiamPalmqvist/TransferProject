# Imports
from tkinter import *
from tkinter.ttk import *
import DatabaseHandler


class sqliteWindow(Tk):

    @staticmethod
    def seats(frame, showID):  # This gets the seats for the layout
        labelLen = [2, 10, 13, 15, 4, 13, 24]

        seatsList = DatabaseHandler.getSeats(showID, True)
        for i in seatsList:
            print(i)

        names = ["Booking ID:", "First Name:", "Last Name:", "Seat Type:", "Seat Booked:", "Phone Number:",
                 "E-mail:"]

        for i in range(7):
            wordLabel = Label(frame)
            wordLabel.config(text=names[i], width=len(names[i]))
            wordLabel.grid(row=0, column=i, sticky='w')

        blankLabel = Label(frame)
        blankLabel.config(text="")
        blankLabel.grid(row=1, column=0)

        ### SETTING THE LAYOUT FOR THE LABELS

        for i in range(len(seatsList)):
            for f in range(7):
                newText = Label(frame)
                if f == 3:
                    if seatsList[i][3] == 0:
                        newText.config(text="Normal Seat", width=labelLen[f])
                    elif seatsList[i][3] == 1:
                        newText.config(text="Discounted Seat", width=labelLen[f])
                    elif seatsList[i][3] == 2:
                        newText.config(text="Special Seat", width=labelLen[f])
                    else:
                        newText.config(text=seatsList[i][f], width=labelLen[f])
                else:
                    newText.config(text=seatsList[i][f], width=labelLen[f])
                newText.grid(row=i + 2, column=f, sticky='w')

    @staticmethod
    def seatsForSearch(frame, name):  # This gets the seats for the layout dependant on the name
        labelLen = [2, 10, 13, 15, 4, 13, 24]

        seatsList = DatabaseHandler.getSeatsSearch(name)
        for i in seatsList:
            print(i)

        names = ["Booking ID:", "First Name:", "Last Name:", "Seat Type:", "Seat Booked:", "Phone Number:",
                 "E-mail:"]

        for i in range(7):
            wordLabel = Label(frame)
            wordLabel.config(text=names[i], width=len(names[i]))
            wordLabel.grid(row=0, column=i, sticky='w')

        blankLabel = Label(frame)
        blankLabel.config(text="")
        blankLabel.grid(row=1, column=0)

        ### SETTING THE LAYOUT FOR THE LABELS

        for i in range(len(seatsList)):
            for f in range(7):
                newText = Label(frame)
                if f == 3:
                    if seatsList[i][3] == 0:
                        newText.config(text="Normal Seat", width=labelLen[f])
                    elif seatsList[i][3] == 1:
                        newText.config(text="Discounted Seat", width=labelLen[f])
                    elif seatsList[i][3] == 2:
                        newText.config(text="Special Seat", width=labelLen[f])
                    else:
                        newText.config(text=seatsList[i][f], width=labelLen[f])
                else:
                    newText.config(text=seatsList[i][f], width=labelLen[f])
                newText.grid(row=i + 2, column=f, sticky='w')

    @staticmethod
    def getRev(showList):  # This gets the revenue of the performances so I don't have to repeat it a lot later
        revenue = 0
        for i in range(len(showList)):
            if showList[i][3] == 0:
                revenue += 10
            elif showList[i][3] == 1:
                revenue += 5
        return revenue

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

        ### SETTING UP THE NOTEBOOKS USING TKINTER.TKK ###

        tabControl = Notebook(window)
        Notebook(master=None)

        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tab3 = Frame(tabControl)
        tab4 = Frame(tabControl)
        tab5 = Frame(tabControl)
        tabControl.add(tab1, text='Show 1')
        tabControl.add(tab2, text='Show 2')
        tabControl.add(tab3, text='Show 3')
        tabControl.add(tab4, text='Show Information')
        tabControl.add(tab5, text='Search for Ticketholder')
        tabControl.pack(expand=1, fill='both')

        frame1 = Frame(tab1)
        frame1.pack()

        frame2 = Frame(tab2)
        frame2.pack()

        frame3 = Frame(tab3)
        frame3.pack()

        frame4 = Frame(tab4)
        frame4.pack()

        frame5 = Frame(tab5)
        frame5.pack()

        ### END OF SETTING UP THE NOTEBOOKS USING TKINTER.TTK ###

        ### PAGE 1 ###

        page1 = Frame(frame1)
        page1.pack(expand=True)
        self.seats(page1, '0')

        ### END OF PAGE 1 ###

        ### PAGE 2 ###

        page2 = Frame(frame2)
        page2.pack(expand=True)
        self.seats(page2, '1')

        ### END OF PAGE 2 ###

        ### PAGE 3 ###

        page3 = Frame(frame3)
        page3.pack(expand=True)
        self.seats(page3, '2')

        ### END OF PAGE 3 ###

        ### PAGE 4 ###

        page4 = Frame(frame4)
        page4.pack(expand=True)

        seatsList0 = DatabaseHandler.getSeats("0", True)
        seatsList1 = DatabaseHandler.getSeats("1", True)
        seatsList2 = DatabaseHandler.getSeats("2", True)
        seatsList3 = (len(seatsList0) + len(seatsList1) + len(seatsList2))

        labelList = ["", "Seats Sold", "Seats Left", "Revenue"]
        labelList2 = ["Show 1:", "Show 2:", "Show 3:", "Total:"]

        seatsRev0 = self.getRev(seatsList0)
        seatsRev1 = self.getRev(seatsList1)
        seatsRev2 = self.getRev(seatsList2)

        labelList3 = [[len(seatsList0), (200 - len(seatsList0)), ("£" + str(seatsRev0))],
                      [len(seatsList1), (200 - len(seatsList1)), ("£" + str(seatsRev1))],
                      [len(seatsList2), (200 - len(seatsList2)), ("£" + str(seatsRev2))],
                      [seatsList3, 600 - seatsList3, ("£" + str(seatsRev0 + seatsRev1 + seatsRev2))]]

        for i in range(4):
            # Breaking up the Labels in the same loop
            textLabel = Label(page4)
            textLabel.config(text=labelList[i], width=10)  # For the headings
            textLabel.grid(row=0, column=i)

            textLabel = Label(page4)
            textLabel.config(text=labelList2[i], padding=10)  # For the titles of the information
            textLabel.grid(row=i + 1, column=0)

            for f in range(3):
                textLabel = Label(page4)
                textLabel.config(text=labelList3[i][f], padding=10)  # For the information in the boxes
                textLabel.grid(row=i + 1, column=f + 1)

        ### END OF PAGE 4 ###

        ### START OF PAGE 5 ###

        # Start of defining frames

        frameAbove = Frame(tab5)
        frameAbove.pack(side=TOP, expand=False)

        frameBelow = Frame(tab5)
        frameBelow.pack(side=TOP, expand=False)

        # End of defining frames

        # Defining the button that will ask for the names form the database

        searchLabel = Label(frameAbove, text="Student's last name:")
        searchLabel.grid(row=0, column=0)
        self.searchVar = StringVar()
        self.searchVar = Entry(frameAbove)
        self.searchVar.grid(row=0, column=1)
        searchButton = Button(frameAbove, text="Search", takefocus=False, command=lambda: self.seatsForSearch(frameBelow, self.searchVar.get()))
        searchButton.grid(row=0, column=2, padx=10)

        # End of defining the button that will ask for the names form the database

        ### END OF PAGE 5 ###


def main():
    app = sqliteWindow()
    app.mainloop()
