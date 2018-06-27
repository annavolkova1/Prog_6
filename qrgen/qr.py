import uuid
import cairosvg
import pyqrcode
from PIL import Image


def uuid_generator():
    n = uuid.uuid1()
    return n


uuid = str(uuid_generator())

path = r"C:\Users\Anna_Banana\PycharmProjects\untitled3\\"

# Creating qr code
url = pyqrcode.create('http://adultmult.tv/')
url.svg("example.svg", scale=8)

conf = {
    'width': 1200,
    'height': 1200,
}
cairosvg.svg2png(
    file_obj=open('example.svg'),
    write_to='qr.png',
    parent_width=conf['width'],
    parent_height=conf['height'],
    scale=2.8
)
img = Image.open('qr.png')
logo = Image.open('./static/the_simpsons.png')
img.paste(logo, (250, 150), logo)
img = img.crop((0, -50, conf['width'], conf['height']))
img.save(uuid + '.png')
