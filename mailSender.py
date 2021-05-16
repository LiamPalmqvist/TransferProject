import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import imageEdit

port = 465  # For SSL
password = "test4collyers01!"
login = "test4collyers@gmail.com"


def sendMail(recieverEmail, nameF, nameL, seatBooked, day, seatType):

    dayMessage = "15th"
    message = MIMEMultipart()
    message["Subject"] = "Collyer's theatre night booking confirmation"
    message["From"] = login
    message["To"] = recieverEmail

    if day == 1:
        dayMessage = "16th"
    elif day == 2:
        dayMessage = "17th"

    # Create the plain text part of your email

    text = """\
Dear Mr/Mrs {0},

Your seat, {1}, has been reserved for the {2} of July.

Thank you for booking a seat with us."""

    text = text.format(nameL, seatBooked, dayMessage)
    print(text)

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    image = imageEdit.drawImage(nameF, nameL, seatBooked, seatType, day)

    with open(image, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode the file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "content-Disposition",
        f"attachment; filename= {image}",
    )

    message.attach(part)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(login, password)

        # SEND EMAIL HERE

        server.sendmail(login, recieverEmail, message.as_string())

        print("Sending mail to " + recieverEmail)
