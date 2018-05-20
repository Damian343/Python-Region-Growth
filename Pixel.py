#!/usr/bin/python

#pixel class
#keeps track of 
#	x and y of pixel
#	whether been visited or not
#	greyscale value assigned to it

class Pixel:

	def __init__(self, x, y, value, status = False):
		self.x = x
		self.y = y
		self.value = value
		self.status = status
	
	@property
	def status(self):
		return self.status
		
	@property
	def x(self):
		return self.x
	
	@property
	def y(self):
		return self.y

	@property
	def value(self):
	    return self.value
	
	@status.setter
	def status(self, status):
		self.status = status