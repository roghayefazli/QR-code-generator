# QR-code-generator
### QR Code Generator

This Python script `qr.py` uses the `qrcode` library to generate a QR code from a string of text. The generated QR code is saved as a PNG image file named `qrcode.png`.

#### How it Works

The script performs the following steps:

1.  **Import Library:** It imports the `qrcode` library, which is a a popular choice for creating QR codes in Python.
2.  **Define Data:** A multi-line string `data` is defined to contain the information to be encoded. In this example, it includes an email address and a GitHub username. You can easily modify this to include any text, URL, or other information.
3.  **Configure QR Code:** A `qrcode.QRCode` object is created with specific configurations:
      * `version=1`: Specifies the size of the QR code.
      * `error_correction=qrcode.constants.ERROR_CORRECT_L`: Sets the error correction level to low, allowing the QR code to be scanned even if a small portion is damaged.
      * `box_size=10`: Determines the size of each square in the QR code.
      * `border=4`: Sets the width of the white border around the QR code.
4.  **Add Data and Make Image:** The `add_data` method adds the `data` to the QR code object, and `make(fit=True)` fits the QR code to the provided data. An image is then created with black and white colors for the squares and background, respectively.
5.  **Save File:** The `img.save("qrcode.png")` command saves the final QR code image as a PNG file.

#### Requirements

To run this script, you need to install the `qrcode` library. You can do this using pip:

```bash
pip install qrcode
```

#### How to Use

1.  **Install Dependencies:** Make sure you have the `qrcode` library installed.
2.  **Edit the Data:** Open the `qr.py` file and change the content of the `data` variable to the information you want to encode.
3.  **Run the Script:** Execute the script from your terminal:
    ```bash
    python qr.py
    ```
4.  **Find the QR Code:** A new file named `qrcode.png` will be created in the same directory, containing your generated QR code.
