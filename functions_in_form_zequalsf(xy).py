
from PIL import Image
from math import sin, cos

Width = 640
Height = 640

newi = Image.new("RGB", (Width, Height))

def fxyr(x, y):
    return 4 - (x ** 2 + y ** 2)

def fxyg(x, y):
    return 4 - (x ** 2 + y ** 2)

def fxyb(x, y):
    return 4 - (x ** 2 + y ** 2)

def calculate_scaledown(f):
    maxv = f(Width, Height)
    if maxv == 0:
        return 1

    scale = (255 * 64) / maxv
    return scale

ysubtract = -(Height / 2)
xsubtract = -(Width  / 2)

sr = calculate_scaledown(fxyr)
sg = calculate_scaledown(fxyg)
sb = calculate_scaledown(fxyb)

for y in range(Height):
    for x in range(Width):
        r = int(fxyr(x + xsubtract, y + ysubtract) * sr)
        g = int(fxyg(x + xsubtract, y + ysubtract) * sg)
        b = int(fxyb(x + xsubtract, y + ysubtract) * sb)
        newi.putpixel((x,y), (r, g, b))

newi.save("out.png", "PNG")
