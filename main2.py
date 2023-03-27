import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(file_name + ".png")
    print("QR code generated and saved as " + file_name + ".png")

# Example usage
generate_qr_code("www.Flipkart.com", "example_qr_code")
