
from PIL import Image
from random import randrange

# dimensions
width = 640
height = 480

# how much variation in the curves
variation = 100

# point class to describe a point in 2D space
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# main Bezier curve class
class Beziercurve(object):
    def __init__(self, p0, p1, p2, p3):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def at(self, t):
        # this is just to make the math "easier" to read. It won't help.
        p0x, p1x, p2x, p3x = self.p0.x, self.p1.x, self.p2.x, self.p3.x
        p0y, p1y, p2y, p3y = self.p0.y, self.p1.y, self.p2.y, self.p3.y
        # some math which can be found by googling Bezier curve
        x = ((1-t)**3)*p0x + 3*((1-t)**2)*t*p1x + 3*((1-t)*t**2)*p2x + (t**3)*p3x
        
        # decided to just use x
        # y = ((1-t)**3)*p0y + 3*((1-t)**2)*t*p1y + 3*((1-t)*t**2)*p2y + (t**3)*p3y
        
        # limit so it doesn't go offscreen and cause an error
        if x < 0:
            x = 0
        if x > width-1:
            x = width-1
        return x

# point at top of screen with random x coordinate
top = Point(randrange(0, width), 0)
# point at the bottom of the screen with random x coordinate
bottom = Point(randrange(0, width), height-1)
# this point changes the curvature, I'll just randomize it relative to the top point
toprandom = Point(top.x + randrange(-variation, variation), top.y + randrange(-variation, variation))
# this point changes the curvature, I'll just randomize it relative to the bottom point.
bottomrandom = Point(bottom.x + randrange(-variation, variation), bottom.y + randrange(-variation, variation))

# Create the Bezier curve class and give it values
curve = Beziercurve(bottomrandom, bottom, top, toprandom)

# create a new image
newimg = Image.new("RGB", (width, height))

# You want it to increment in 0.1 not 1 so times height by ten then divided t by 10
for t in range(height * 10):
    t /= 10
    # input to curve.at has to be between 0 and 1, hence divide t by height.
    x, y = curve.at(t / height), t
    # add the pixel to the image
    newimg.putpixel((int(x), int(y)), (255, 255, 255))

# save the file.
newimg.save("Curve.png", "PNG")
newimg.close()
