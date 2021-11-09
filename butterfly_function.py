
from PIL import Image
import math

WIDTH = 640
HEIGHT = 640

def fxy(x, y):
        if x == 0 and y == 0:
            x = 1
            y = 1
        return ((x ** 2 - y ** 2) * math.sin((x + y) / 1.5)) / (x ** 2 + y ** 2)

def next_img(fn, STRETCH):

    img = Image.new("RGB", (WIDTH, HEIGHT))

    xorigin = -(WIDTH / 2)
    yorigin = -(HEIGHT / 2)

    SCALE = 400

    COLORSPEED = 0.05


    for y in range(HEIGHT):
        for x in range(WIDTH):
            xcoord = x + xorigin
            ycoord = y + yorigin

            grayscale = int(fxy(xcoord * STRETCH, ycoord * STRETCH) * SCALE)

            divisor = grayscale // 255

            r = 127 + math.sin(grayscale * COLORSPEED) * 127
            g = 127 + math.sin((grayscale * COLORSPEED) + (math.pi / 2)) * 127
            b = 127 + math.cos(grayscale * COLORSPEED) * 127

            img.putpixel((x, y), (int(r), int(g), int(b)))

    img.save("frames//{}.png".format(fn), "PNG")
    img.close()

for i in range(1000):
    next_img(i, (i / 10000) + 0.0001)



