import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size = 10,
    border = 4,
)

data = """Hello Habiby
Don't forget to smile :)
I hope you have a good day
From: Zeyad Mohamad Ezzat Basha

-- Using Python --"""

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=(45, 100, 255), back_color="black")
img.save("QRCODE.png")