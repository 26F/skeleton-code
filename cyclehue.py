
from math import sqrt, cos, sin, radians
from PIL import Image

# limit the rgb values between [0,255] inclusive.
def limit(v):
	if v < 0:
		return 0
	if v > 255:
		return 255
	# round up
	return int(v + 0.5)

# class to represent a "pixel" composed of rgb values
class rgbpixel(object):
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

# class that does the hue shifting. Found it on stackoverflow.
# https://stackoverflow.com/questions/8507885/shift-hue-of-an-rgb-color
class HueShifter(object):
	def __init__(self):
		self.matrix = [[1,0,0], [0,1,0], [0,0,1]]

	def set_hue_rotation(self, degrees):
		cosA = cos(radians(degrees))
		sinA = sin(radians(degrees))

		self.matrix[0][0] = cosA + (1.0 - cosA) / 3.0
		self.matrix[0][1] = 1.0 / 3.0 * (1.0 - cosA) - sqrt(1.0 / 3.0) * sinA
		self.matrix[0][2] = 1.0 / 3.0 * (1.0 - cosA) + sqrt(1.0 / 3.0) * sinA
		self.matrix[1][0] = 1.0 / 3.0 * (1.0 - cosA) + sqrt(1.0 / 3.0) * sinA
		self.matrix[1][1] = cosA + 1.0 / 3.0*(1.0 - cosA)
		self.matrix[1][2] = 1.0 / 3.0 * (1.0 - cosA) - sqrt(1.0 / 3.0) * sinA
		self.matrix[2][0] = 1.0 / 3.0 * (1.0 - cosA) - sqrt(1.0 / 3.0) * sinA
		self.matrix[2][1] = 1.0 / 3.0 * (1.0 - cosA) + sqrt(1.0 / 3.0) * sinA
		self.matrix[2][2] = cosA + 1.0 / 3.0 * (1.0 - cosA)

	def apply(self, rgbpixel):
		r, g, b = rgbpixel.r, rgbpixel.g, rgbpixel.b
		rx = r * self.matrix[0][0] + g * self.matrix[0][1] + b * self.matrix[0][2]
		gx = r * self.matrix[1][0] + g * self.matrix[1][1] + b * self.matrix[1][2]
		bx = r * self.matrix[2][0] + g * self.matrix[2][1] + b * self.matrix[2][2]
		return limit(rx), limit(gx), limit(bx)

# open an image to hue shift.
inputimage = Image.open("Superbike.jpg")

# create a "hue shifter"
hueshifter = HueShifter()

# get the dimensions of the image
width, height = inputimage.size

# how much to shift the hue
hueshifter.set_hue_rotation(100)

# for every pixel in the image apply the hue shift
for y in range(height):
	for x in range(width):
		# get the pixel rgb values
		r, g, b = inputimage.getpixel((x, y))
		# create the rgbpixel
		rgbp = rgbpixel(r, g, b)
		# apply the rotation
		r, g, b = hueshifter.apply(rgbp)
		# set the pixel to the new RGB values
		inputimage.putpixel((x, y), (int(r), int(g), int(b)))

# save the image
inputimage.save("c_shifted.png", "PNG")

# close the file.
inputimage.close()