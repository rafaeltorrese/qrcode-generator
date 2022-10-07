import os

from dotenv import load_dotenv
from qrcode import QRCode


load_dotenv()

url = os.getenv('MY_URL')

print(url)
qr = QRCode(version=1, box_size=10, border=5)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('advisoring-qr.png')