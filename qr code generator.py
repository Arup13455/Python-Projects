import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="yellow", back_color="white")
    img.save("qrimg003.png")


url = input("Enter your url:")
generate_qrcode(url)
