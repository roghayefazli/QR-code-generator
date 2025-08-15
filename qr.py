import qrcode

# Data to be encoded in the QR code
data = '''E-mail : roghayefazlii@gmail.com
github : roghayefazli
'''

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (controls the size)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border thickness around the QR code
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
