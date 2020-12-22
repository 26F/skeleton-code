
from PIL import Image

asciiColorTable = "#MWwnv+-:. "

# calculate the indices
colorscalefactor = (len(asciiColorTable)-1) / 255
print(colorscalefactor)

# input file. You can use an image you like
inputfile = "Superbike.jpg"
# open image
inputimage = Image.open(inputfile)
# convert to greyscale
img = inputimage.convert('L')

# get the dimensions of the image
Width, Height = img.size

# width in characters
ncharacterswide = 120

# resize the image so the ascii art will have a max of ncharacterswide
# characters in width. Height is scaled to match the dimensions
# as well

scalefactor = ncharacterswide / Width

# resize the image
img = img.resize((int(Width * scalefactor), int((Height * scalefactor) / 2)), Image.ANTIALIAS)

asciistring = ""

outputtxt = open("ascii_art.txt", 'w')
for y in range(int((Height * scalefactor) / 2)):
	for x in range(int(Width * scalefactor)):
		asciiindex = int(img.getpixel((x, y)) * colorscalefactor)
		asciistring += asciiColorTable[asciiindex]
	asciistring += '\n'

outputtxt.write(asciistring)
outputtxt.close()
		






