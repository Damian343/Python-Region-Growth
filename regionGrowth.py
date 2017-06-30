#Author: Damian Hamilton
#date  : Mar, 16 2017
#COSC 416

import random
from Pixel import Pixel
from PIL import Image

###################################################
##region growth, pick random seed(pixel)
##let the color value at that place be the 
##the color we want to define a region within
##create minimum and max based on difference of threshold
##keep searching around till no more pixels fit in 
##threshold 
###################################################

#wanted color for region
selectedColor= 255#white
#image you wish to use
desiredImage = 'sample2.jpg'
#how much region we will accept
#greater the threshold the greater the region
threshold    = 30
minimum      = 0
maximum      = 0
h			 = 0
w            = 0
	

def setup():
	global currentPixel, minimum, maximum, h, w, desiredImage

	img = Image.open(desiredImage)
	grey = img.convert('L')
	pxlValueMap = grey.load()
	
	w = grey.size[0]
	h = grey.size[1]
	#pick a random seed, depending on width and height of img
	seedX = random.randint(0,w)
	seedY = random.randint(0,h)
	
	pixels = [[Pixel(x,y,pxlValueMap[x,y]) for x in range(w)] for y in range(h)]
	#get minimum and max from threshold difference
	currentColor = pxlValueMap[seedX, seedY]
	minimum      = currentColor - threshold
	maximum      = currentColor + threshold
	#choose random seed to be our origin
	currentPixel = pixels[seedY][seedX]

	process(currentPixel, pxlValueMap, pixels)
	print("visualizing...")

	finish(grey)

def process(currentPixel, valueMap, pixels):
	stillSearching = True
	##allows us to backtrack visited pixels
	stack = []

	while stillSearching:
		currentPixel.status = True

		nextPixel = check_Neighbors(pixels, currentPixel)
		if(nextPixel is not None):
			
			valueMap[nextPixel.x, nextPixel.y] = selectedColor

			stack.append(currentPixel)

			currentPixel = nextPixel

		elif (len(stack) > 0):
			currentPixel = stack[-1]
			stack.pop(-1)
		else:
			stillSearching = False

#checks the 4 neighboring pixels to see if they
#	-exist
#	-been visited 
#	-between minimum and maximum threshold
def check_Neighbors(pixels, currentPixel):
	global minimum, maximum
	
	neighbors = []
	x = currentPixel.x
	y = currentPixel.y

	if safe_index(x, y+1):
		  top   = pixels[y+1][x]
	else: top = Pixel(0, 0, 0, True)

	if safe_index(x+1, y):
		  right = pixels[y][x+1]
	else: right = Pixel(0, 0, 0, True)

	if safe_index(x, y-1):
		  down  = pixels[y-1][x]
	else: down = Pixel(0, 0, 0, True)

	if safe_index(x-1, y):
		  left  = pixels[y][x-1]
	else: left = Pixel(0, 0, 0, True)
	
	if(not top.status   and top.value   > minimum  and top.value   < maximum):
		neighbors.append(top)
	if(not right.status and right.value > minimum  and right.value < maximum):
		neighbors.append(right)
	if(not down.status  and down.value  > minimum  and down.value  < maximum):
		neighbors.append(down)
	if(not left.status  and left.value  > minimum  and left.value  < maximum):
		neighbors.append(left)

	#pick random neighbor to check 
	if(len(neighbors) > 0):
		r = random.randint(0, len(neighbors)-1)
		return neighbors[r]
	else:
		return None

def safe_index(x, y):
	global w,h
	if(x < w and x >= 0 and y < h and y >= 0):
		return True
	else:
		return False
	
def finish(finishedImage):
	finishedImage.show()
	finishedImage.save("finished.png")
		
print("running...")
setup()
