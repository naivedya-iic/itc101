"""
QR Code Generator
------------------
Converts text or a URL into a QR code image.

Install dependency:
    pip install qrcode[pil]

Usage: python 27_qr_generator.py
"""

import qrcode


def generate_qr(data, filename="qrcode.png", box_size=10, border=4,
                 fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    return filename


def main():
    print("=== QR CODE GENERATOR ===")

    while True:
        data = input("\nEnter text or URL to encode (or 'q' to quit): ").strip()
        if data.lower() == "q":
            print("Goodbye!")
            break
        if not data:
            print("Please enter some text.")
            continue

        filename = input("Output filename (default: qrcode.png): ").strip()
        filename = filename if filename else "qrcode.png"
        if not filename.lower().endswith(".png"):
            filename += ".png"

        try:
            saved_path = generate_qr(data, filename)
            print(f"QR code saved as '{saved_path}'")
        except Exception as e:
            print(f"Error generating QR code: {e}")


if __name__ == "__main__":
    main()
