import qrcode
from PIL import Image
import requests
from io import BytesIO


def generate_qr_with_url(url, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(output_path)

def display_image_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.show()
    else:
        print("Failed to retrieve image")

def main():
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMHnkJVxJHUw02oli7X-COnTSlF_yD-2WtzQ&s"  
    qr_data = image_url 
    output_path = "niu.png"
    generate_qr_with_url(qr_data, output_path)

    
    print("QR Code Generated. Scan the QR code with a QR code scanner to display the image.")
    display_image_from_url(image_url)

if __name__ == "__main__":
    main()
