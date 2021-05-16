from PIL import Image, ImageFont, ImageDraw
import random


def drawImage(firstName, lastName, seat, bookingType, day):

    pricePaid = "£10.00"
    dayBooked = "July 15 2020"
    seatType = "Normal"
    num = random.randint(0, 4)
    imgList = ["assets/first.png", "assets/second.png", "assets/third.png", "assets/fourth.png", "assets/fifth.png"]
    image = Image.open(imgList[num])
    font = ImageFont.truetype("assets/Montserrat-Medium.ttf", 24)

    if bookingType == 1:
        pricePaid = "£5.00"
    elif bookingType == 2:
        pricePaid = "£0.00"

    if bookingType == 1:
        seatType = "Discounted"
    elif bookingType == 2:
        seatType = "Special"

    if day == 1:
        dayBooked = "July 16 2020"
    elif day == 2:
        dayBooked = "July 17 2020"

    # Positions are Lastname, 222, 362; Seat, 52, 472; Seat type, 222, 472; Price Paid, 52, 582; Day booked, 222, 582

    image_editable = ImageDraw.Draw(image)
    image_editable.text((52, 362), firstName, (0, 0, 0), font=font)
    image_editable.text((222, 362), lastName, (0, 0, 0), font=font)
    image_editable.text((52, 472), seat, (0, 0, 0), font=font)
    image_editable.text((222, 472), seatType, (0, 0, 0), font=font)
    image_editable.text((52, 582), pricePaid, (0, 0, 0), font=font)
    image_editable.text((222, 582), dayBooked, (0, 0, 0), font=font)

    image.save("Ticket.png")

    return "Ticket.png"
