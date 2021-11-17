


from PIL import Image
import colorsys

colorhash = dict()

colors = 256
hue = 0.0
step = 1.0 / colors

for gray in range(colors):
    rgb = colorsys.hsv_to_rgb(hue, 1,1)
    hue += step

    r = round(rgb[0] * 255)
    g = round(rgb[1] * 255)
    b = round(rgb[2] * 255)

    colorhash[gray] = (r, g, b)

inputimg = Image.open("s.jpg", "r")

width, height = inputimg.size

outputimg = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        col = inputimg.getpixel((x,y))
        if type(col) == tuple:
            gray = col[0]
        else:
            gray = col
        r, g, b = colorhash[gray]
        outputimg.putpixel((x,y), (r, g, b))

outputimg.save("tigercolor.png", "PNG")
inputimg.close()
outputimg.close()
