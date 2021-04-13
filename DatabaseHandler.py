import sqlite3

def insert(nameF, nameL, seatType, showID, seatBooked, phoneNum, eMail):
    con = sqlite3.connect("transferDB.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO TransferTable (nameF, nameL, seatType, showID, seatBooked, phoneNum, eMail) VALUES ('" + nameF.title() + "', '" + nameL.title() + "', " + str(
            seatType) + ", " + str(showID) + ", '" + seatBooked + "', '" + phoneNum + "', '" + eMail + "')")

    con.commit()

    # cur.execute("SELECT * FROM TransferTable")


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

    else:
        cur.execute("SELECT bookingID, nameF, nameL, seatType, seatBooked, phoneNum, eMail FROM transferTable WHERE showID = " + showID + " ORDER BY nameL")
        seatsTuple = cur.fetchall()

        print(seatsTuple)

        return seatsTuple
