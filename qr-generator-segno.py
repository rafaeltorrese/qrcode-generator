import os
from dotenv import load_dotenv
from segno import helpers

load_dotenv()

# url = os.getenv('MY_URL')

qrcode = helpers.make_vcard(
    name=os.getenv('NAME'), 
    displayname=os.getenv('DISPLAY_NAME'),
    email=os.getenv('EMAIL'),    
)

qrcode.save('my-vcard.png', scale=20, border=1)