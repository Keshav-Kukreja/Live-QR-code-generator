import segno
from urllib.request import urlopen

# variables
img="img.gif"
file_name="qr.gif"

# main section
slts_qrcode = segno.make_qr("Data never lies!")

slts_qrcode.to_artistic(
    background=img,
    target=file_name,
    scale=10,
    light="#f5f5f5",
    dark="#011d14",
    data_dark="#011d14",
    data_light="#f5f5f5",
)