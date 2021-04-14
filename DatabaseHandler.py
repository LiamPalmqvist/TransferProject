# Imports
import sqlite3

# Inserts the data into the SQLite table known as transferDB.db
def insert(nameF, nameL, seatType, showID, seatBooked, phoneNum, eMail):
    con = sqlite3.connect("transferDB.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO TransferTable (nameF, nameL, seatType, showID, seatBooked, phoneNum, eMail) VALUES ('" + nameF.title() + "', '" + nameL.title() + "', " + str(
            seatType) + ", " + str(showID) + ", '" + seatBooked + "', '" + phoneNum + "', '" + eMail + "')")

    con.commit()

    # cur.execute("SELECT * FROM TransferTable")

# This gets the seatIDs for the shows from the SQLite table known as transferDB.db
def getSeats(showID, getForLayout):
    con = sqlite3.connect("transferDB.db")
    cur = con.cursor()
    if not getForLayout:
        cur.execute("SELECT seatBooked FROM transferTable WHERE showID = " + showID)
        seatsTuple = cur.fetchall()
        seatsTaken = []
        for i in seatsTuple:
            seatsTaken.append(''.join(i))

        return seatsTaken

    # Function for the SQLiteShow.py file to get the entire Database instead of just the seat IDs
    else:
        cur.execute("SELECT bookingID, nameF, nameL, seatType, seatBooked, phoneNum, eMail FROM transferTable WHERE showID = " + showID + " ORDER BY nameL")
        seatsTuple = cur.fetchall()

        return seatsTuple

def getSeatsSearch(name):  # This gets the seats for the layout dependant on the name
    con = sqlite3.connect("transferDB.db")
    cur = con.cursor()

    cur.execute("SELECT bookingID, nameF, nameL, seatType, seatBooked, phoneNum, eMail FROM transferTable WHERE nameL = '" + name + "'")
    seatsTuple = cur.fetchall()

    return seatsTuple