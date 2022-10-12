import os

from dotenv import load_dotenv
from qrcode import QRCode


load_dotenv()

# url = os.getenv('MY_URL')
text = os.getenv('MY_TEXT')
email = os.getenv('SEND_EMAIL')
qr = QRCode(version=1, box_size=10, border=5)

qr.add_data(email)
# qr.add_data('\n\n')
# qr.add_data(os.getenv('LINK2'))
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qr.png')