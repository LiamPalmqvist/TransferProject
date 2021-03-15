import sqlite3


def insert(self, nameF, nameL, seatType, showID, seatBooked, phoneNum, eMail):
    con = sqlite3.connect("transferDB.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO TransferTable (nameF, nameL, seatType, showID, seatBooked, phoneNum, eMail) VALUES ('" + nameF + "', '" + nameL + "', " + str(
            seatType) + ", " + str(showID) + ", '" + seatBooked + "', '" + phoneNum + "', '" + eMail + "')")

    con.commit()

    # cur.execute("SELECT * FROM TransferTable")


def getSeats():
    con = sqlite3.connect("transferDB.db")
    cur = con.cursor()
    cur.execute("SELECT seatBooked FROM transferTable")
    seatsTuple = cur.fetchall()
    seatsTaken = []
    for i in seatsTuple:
        seatsTaken.append(''.join(i))

    return seatsTaken
