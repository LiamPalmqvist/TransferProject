from tkinter import *
from tkinter.ttk import *
import DatabaseHandler
import SQLiteShow

LARGE_FONT = ("Verdana", 12)


class SeatsView(Tk):

    def __init__(self):
        Tk.__init__(self)
        window = Frame(self)

        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Defining config within the master window
        Tk.configure(self, bg='ivory2')
        Tk.title(self, "Booking GUI")
        Tk.option_add(self, '*Font', 'helvetica 14')
        Tk.option_add(self, '*Background', 'ivory2')
        Tk.geometry(self, '800x700+600+300')
        # End of defining within master window

        self.frames = {}

        for i in (SeatsOne, SeatsTwo, SeatsThree):  # This is where the other frames will go once defined
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SeatsOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class SeatsOne(Frame):

    def book(self):
        seatBooked = self.radioSelect.get()
        seatType = self.ticketType.get()
        email = self.emailEntry.get()
        nameF = self.fNameEntry.get()
        nameL = self.lNameEntry.get()
        mobile = self.numberEntry.get()
        DatabaseHandler.insert(self, nameF, nameL, seatType, 0, seatBooked, mobile, email)

    def seats(self, alph, frame2b, showID):
        seatsTaken = DatabaseHandler.getSeats(showID, False)
        for i in range(10):
            for f in range(20):
                newButton = Radiobutton(frame2b)
                newButton.config(variable=self.radioSelect, value=(str(alph[i]) + str(f + 1)), takefocus=False)
                if ((str(alph[i])) + str(f + 1)) in seatsTaken:
                    newButton.config(state=DISABLED)

                newButton.grid(row=i + 1, column=f + 1)
        self.radioSelect.get()
        self.radioSelect.set(' ')

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack()

        # Frames inside MASTER
        frame1top = Frame(frame)
        frame1top.pack(side=TOP)

        frame1middle = Frame(frame)
        frame1middle.pack(side=BOTTOM, fill=Y)

        # Frames inside frame1middle
        frame2a = Frame(frame1middle)
        frame2a.pack(side=LEFT)

        frame2b = Frame(frame1middle)
        frame2b.pack()

        frame2c = Frame(frame1middle)
        frame2c.pack(fill=Y)

        # Frames inside frame2C
        frame2ca = Frame(frame2c)
        frame2ca.pack(side=TOP, fill=BOTH)

        frame2cb = Frame(frame2c)
        frame2cb.pack(side=LEFT)

        frame2d = Frame(frame1middle)
        frame2d.pack(side=BOTTOM)
        ### End of frames

        ### Labelling and making radio buttons
        header = Label(frame1top)
        header.config(borderwidth=0, text="""
                Please select your seat below.

                """)
        header.pack()

        # This is what makes the 1 - 20 above the buttons
        for i in range(20):
            num = Label(frame2b)
            num.config(text=i + 1)
            num.grid(column=i + 1, row=0)

        # This is what makes the A - K along side the buttons
        alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        for i in range(10):
            num = Label(frame2b)
            num.config(text=alph[i])
            num.grid(column=0, row=i + 1)

        # Seating is in the frame 2B and is made by this "for in range" loop

        self.radioSelect = StringVar(parent)
        self.seats(alph, frame2b, "0")

        # Showing the selected seat when the radio buttons are pressed
        seatLabel = Label(frame2ca)
        seatLabel.config(text="Your selected seat is:")
        seatLabel.pack(side=LEFT)

        seatSelected = Label(frame2ca)
        seatSelected.config(textvariable=self.radioSelect)
        seatSelected.pack(side=LEFT)

        # Ticket types
        self.ticketType = IntVar(parent)
        self.ticketType.set(0)
        normalRad = Radiobutton(frame2cb, text="Normal ticket", variable=self.ticketType, value=0, takefocus=False)
        seniorRad = Radiobutton(frame2cb, text="Senior ticket", variable=self.ticketType, value=1, takefocus=False)
        specialRad = Radiobutton(frame2cb, text="Special ticket", variable=self.ticketType, value=2, takefocus=False)
        normalRad.grid(row=0, column=0, sticky=W)
        seniorRad.grid(row=1, column=0, sticky=W)
        specialRad.grid(row=2, column=0, sticky=W)

        ### Text entry

        # Name entry
        fNameText = Label(frame2cb)
        fNameText.config(text="First Name:")
        fNameText.grid(row=3, column=0)
        self.fNameEntry = Entry(frame2cb)
        self.fNameEntry.grid(row=3, column=1)

        lNameText = Label(frame2cb)
        lNameText.config(text="Last Name:")
        lNameText.grid(row=3, column=2, sticky=W)
        self.lNameEntry = Entry(frame2cb)
        self.lNameEntry.grid(row=3, column=3)

        # eMail entry
        emailText = Label(frame2cb)
        emailText.config(text="eMail*:")
        emailText.grid(row=4, column=0, sticky=W)
        self.email = StringVar(parent)
        self.email.set("")
        self.emailEntry = Entry(frame2cb)
        self.emailEntry.grid(row=4, column=1)

        # Mobile number entry
        numberText = Label(frame2cb)
        numberText.config(text="Phone Number*:")
        numberText.grid(row=4, column=2)
        self.numberEntry = Entry(frame2cb)
        self.numberEntry.grid(row=4, column=3)
        ### End of Text Entry

        # Spacing
        spacer = Label(frame2d)
        spacer.config(text="")
        spacer.grid(row=0, column=0)

        # Finalise Button
        bookButton = Button(frame2d)
        bookButton.config(text="BOOK", command=lambda: [self.book(), self.seats(alph, frame2b, "0")])
        bookButton.grid(row=1, column=0)

        # Switching Button
        switchButton = Button(frame2d)
        switchButton.config(text="SHOW 2", command=lambda: controller.show_frame(SeatsTwo))
        switchButton.grid(row=2, column=0)

        show3 = Button(frame2d)
        show3.config(text="SHOW 3", command=lambda: controller.show_frame(SeatsThree))
        show3.grid(row=3, column=0)

        # Button that shows the SQLite table
        tableButton = Button(frame2d)
        tableButton.config(text="Show Bookings", command=lambda: SQLiteShow.main())
        tableButton.grid(row=4, column=0)


class SeatsTwo(Frame):

    def book(self):
        seatBooked = self.radioSelect.get()
        seatType = self.ticketType.get()
        email = self.emailEntry.get()
        nameF = self.fNameEntry.get()
        nameL = self.lNameEntry.get()
        mobile = self.numberEntry.get()
        DatabaseHandler.insert(self, nameF, nameL, seatType, 1, seatBooked, mobile, email)

    def seats(self, alph, frame2b, showID):
        seatsTaken = DatabaseHandler.getSeats(showID, False)
        for i in range(10):
            for f in range(20):
                newButton = Radiobutton(frame2b)
                newButton.config(variable=self.radioSelect, value=(str(alph[i]) + str(f + 1)), takefocus=False)
                if ((str(alph[i])) + str(f + 1)) in seatsTaken:
                    newButton.config(state=DISABLED)

                newButton.grid(row=i + 1, column=f + 1)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack()

        # Frames inside MASTER
        frame1top = Frame(frame)
        frame1top.pack(side=TOP)

        frame1middle = Frame(frame)
        frame1middle.pack(side=BOTTOM, fill=Y)

        # Frames inside frame1middle
        frame2a = Frame(frame1middle)
        frame2a.pack(side=LEFT)

        frame2b = Frame(frame1middle)
        frame2b.pack()

        frame2c = Frame(frame1middle)
        frame2c.pack(fill=Y)

        # Frames inside frame2C
        frame2ca = Frame(frame2c)
        frame2ca.pack(side=TOP, fill=BOTH)

        frame2cb = Frame(frame2c)
        frame2cb.pack(side=LEFT)

        frame2d = Frame(frame1middle)
        frame2d.pack(side=BOTTOM)
        ### End of frames

        ### Labelling and making radio buttons
        header = Label(frame1top)
        header.config(borderwidth=0, text="""
                Please select your seat below.

                """)
        header.pack()

        # This is what makes the 1 - 20 above the buttons
        for i in range(20):
            num = Label(frame2b)
            num.config(text=i + 1)
            num.grid(column=i + 1, row=0)

        # This is what makes the A - K along side the buttons
        alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        for i in range(10):
            num = Label(frame2b)
            num.config(text=alph[i])
            num.grid(column=0, row=i + 1)

        # Seating is in the frame 2B and is made by this "for in range" loop

        self.radioSelect = StringVar(parent)
        self.seats(alph, frame2b, "1")
        self.radioSelect.set(' ')

        # Showing the selected seat when the radio buttons are pressed
        seatLabel = Label(frame2ca)
        seatLabel.config(text="Your selected seat is:")
        seatLabel.pack(side=LEFT)

        seatSelected = Label(frame2ca)
        seatSelected.config(textvariable=self.radioSelect)
        seatSelected.pack(side=LEFT)

        # Ticket types
        self.ticketType = IntVar(parent)
        self.ticketType.set(0)
        normalRad = Radiobutton(frame2cb, text="Normal ticket", variable=self.ticketType, value=0, takefocus=False)
        seniorRad = Radiobutton(frame2cb, text="Senior ticket", variable=self.ticketType, value=1, takefocus=False)
        specialRad = Radiobutton(frame2cb, text="Special ticket", variable=self.ticketType, value=2, takefocus=False)
        normalRad.grid(row=0, column=0, sticky=W)
        seniorRad.grid(row=1, column=0, sticky=W)
        specialRad.grid(row=2, column=0, sticky=W)

        ### Text entry

        # Name entry
        fNameText = Label(frame2cb)
        fNameText.config(text="First Name:")
        fNameText.grid(row=3, column=0)
        self.fNameEntry = Entry(frame2cb)
        self.fNameEntry.grid(row=3, column=1)

        lNameText = Label(frame2cb)
        lNameText.config(text="Last Name:")
        lNameText.grid(row=3, column=2, sticky=W)
        self.lNameEntry = Entry(frame2cb)
        self.lNameEntry.grid(row=3, column=3)

        # eMail entry
        emailText = Label(frame2cb)
        emailText.config(text="eMail*:")
        emailText.grid(row=4, column=0, sticky=W)
        self.email = StringVar(parent)
        self.email.set("")
        self.emailEntry = Entry(frame2cb)
        self.emailEntry.grid(row=4, column=1)

        # Mobile number entry
        numberText = Label(frame2cb)
        numberText.config(text="Phone Number*:")
        numberText.grid(row=4, column=2)
        self.numberEntry = StringVar(parent)
        self.numberEntry.set("")
        self.numberEntry = Entry(frame2cb)
        self.numberEntry.grid(row=4, column=3)
        ### End of Text Entry

        # Spacing
        spacer = Label(frame2d)
        spacer.config(text="")
        spacer.grid(row=0, column=0)

        # Finalise Button
        bookButton = Button(frame2d)
        bookButton.config(text="BOOK", command=lambda: [self.book(), self.seats(alph, frame2b, "1")])
        bookButton.grid(row=1, column=0)

        # Switching Button
        switchButton = Button(frame2d)
        switchButton.config(text="SHOW 1", command=lambda: controller.show_frame(SeatsOne))
        switchButton.grid(row=2, column=0)

        show3 = Button(frame2d)
        show3.config(text="SHOW 3", command=lambda: controller.show_frame(SeatsThree))
        show3.grid(row=3, column=0)

        # Button that shows the SQLite table
        tableButton = Button(frame2d)
        tableButton.config(text="Show Bookings", command=lambda: SQLiteShow.main())
        tableButton.grid(row=4, column=0)


class SeatsThree(Frame):

    def book(self):
        seatBooked = self.radioSelect.get()
        seatType = self.ticketType.get()
        email = self.emailEntry.get()
        nameF = self.fNameEntry.get()
        nameL = self.lNameEntry.get()
        mobile = self.numberEntry.get()
        DatabaseHandler.insert(self, nameF, nameL, seatType, 2, seatBooked, mobile, email)

    def seats(self, alph, frame2b, showID):
        seatsTaken = DatabaseHandler.getSeats(showID, False)
        for i in range(10):
            for f in range(20):
                newButton = Radiobutton(frame2b)
                newButton.config(variable=self.radioSelect, value=(str(alph[i]) + str(f + 1)), takefocus=False)
                if ((str(alph[i])) + str(f + 1)) in seatsTaken:
                    newButton.config(state=DISABLED)

                newButton.grid(row=i + 1, column=f + 1)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack()

        # Frames inside MASTER
        frame1top = Frame(frame)
        frame1top.pack(side=TOP)

        frame1middle = Frame(frame)
        frame1middle.pack(side=BOTTOM, fill=Y)

        # Frames inside frame1middle
        frame2a = Frame(frame1middle)
        frame2a.pack(side=LEFT)

        frame2b = Frame(frame1middle)
        frame2b.pack()

        frame2c = Frame(frame1middle)
        frame2c.pack(fill=Y)

        # Frames inside frame2C
        frame2ca = Frame(frame2c)
        frame2ca.pack(side=TOP, fill=BOTH)

        frame2cb = Frame(frame2c)
        frame2cb.pack(side=LEFT)

        frame2d = Frame(frame1middle)
        frame2d.pack(side=BOTTOM)
        ### End of frames

        ### Labelling and making radio buttons
        header = Label(frame1top)
        header.config(borderwidth=0, text="""
                Please select your seat below.

                """)
        header.pack()

        # This is what makes the 1 - 20 above the buttons
        for i in range(20):
            num = Label(frame2b)
            num.config(text=i + 1)
            num.grid(column=i + 1, row=0)

        # This is what makes the A - K along side the buttons
        alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        for i in range(10):
            num = Label(frame2b)
            num.config(text=alph[i])
            num.grid(column=0, row=i + 1)

        # Seating is in the frame 2B and is made by this "for in range" loop

        self.radioSelect = StringVar(parent)
        self.seats(alph, frame2b, "2")
        self.radioSelect.set(' ')

        # Showing the selected seat when the radio buttons are pressed
        seatLabel = Label(frame2ca)
        seatLabel.config(text="Your selected seat is:")
        seatLabel.pack(side=LEFT)

        seatSelected = Label(frame2ca)
        seatSelected.config(textvariable=self.radioSelect)
        seatSelected.pack(side=LEFT)

        # Ticket types
        self.ticketType = IntVar(parent)
        self.ticketType.set(0)
        normalRad = Radiobutton(frame2cb, text="Normal ticket", variable=self.ticketType, value=0, takefocus=False)
        seniorRad = Radiobutton(frame2cb, text="Senior ticket", variable=self.ticketType, value=1, takefocus=False)
        specialRad = Radiobutton(frame2cb, text="Special ticket", variable=self.ticketType, value=2, takefocus=False)
        normalRad.grid(row=0, column=0, sticky=W)
        seniorRad.grid(row=1, column=0, sticky=W)
        specialRad.grid(row=2, column=0, sticky=W)

        ### Text entry

        # Name entry
        fNameText = Label(frame2cb)
        fNameText.config(text="First Name:")
        fNameText.grid(row=3, column=0)
        self.fNameEntry = Entry(frame2cb)
        self.fNameEntry.grid(row=3, column=1)

        lNameText = Label(frame2cb)
        lNameText.config(text="Last Name:")
        lNameText.grid(row=3, column=2, sticky=W)
        self.lNameEntry = Entry(frame2cb)
        self.lNameEntry.grid(row=3, column=3)

        # eMail entry
        emailText = Label(frame2cb)
        emailText.config(text="eMail*:")
        emailText.grid(row=4, column=0, sticky=W)
        self.email = StringVar(parent)
        self.email.set("")
        self.emailEntry = Entry(frame2cb)
        self.emailEntry.grid(row=4, column=1)

        # Mobile number entry
        numberText = Label(frame2cb)
        numberText.config(text="Phone Number*:")
        numberText.grid(row=4, column=2)
        self.numberEntry = StringVar(parent)
        self.numberEntry.set("")
        self.numberEntry = Entry(frame2cb)
        self.numberEntry.grid(row=4, column=3)
        ### End of Text Entry

        # Spacing
        spacer = Label(frame2d)
        spacer.config(text="")
        spacer.grid(row=0, column=0)

        # Finalise Button
        bookButton = Button(frame2d)
        bookButton.config(text="BOOK", command=lambda: [self.book(), self.seats(alph, frame2b, "2")])
        bookButton.grid(row=1, column=0)

        # Switching Button
        switchButton = Button(frame2d)
        switchButton.config(text="SHOW 1", command=lambda: controller.show_frame(SeatsOne))
        switchButton.grid(row=2, column=0)

        show2 = Button(frame2d)
        show2.config(text="SHOW 2", command=lambda: controller.show_frame(SeatsTwo))
        show2.grid(row=3, column=0)

        # Button that shows the SQLite table
        tableButton = Button(frame2d)
        tableButton.config(text="Show Bookings", command=lambda: SQLiteShow.main())
        tableButton.grid(row=4, column=0)


app = SeatsView()
app.mainloop()
