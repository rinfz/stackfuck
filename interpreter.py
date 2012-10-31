#!/usr/bin/env python

"""

	Stackfuck interpreter:
	Recommended buffers
		* Buffer 0: stdout, standard buffer for copying to, then printing out
		* Buffer 1: stdin, standard buffer for reading user input
		* Buffer 2: stdcheck, standard buffer for checking user input
		* Consider also, further buffers for unique variables and also a temporary buffer.

	More documentation and information can be found at:
		http://esolangs.org/wiki/Stackfuck

"""

class SfCommands:
	def __init__(self):
		"""
			Initialise various data which might be useful
		"""
		self.STACKSIZE = 1024
		self.PUSHINTMAX = 999
		self.bufferCount = 0
		self.currentBuffer = ""
		# list of buffers, not buffer data
		self.bufferArray = []
		self.stack = []
		self.currentBufferData = {}

	def push(self, v):
		"""
			Push character on to stack
				* xxx - number, e.g. P010
				* xC  - character, e.g. PxH (pushes H to stack)
		"""
		if isinstance(v,(int,long)):
			# if integer
			if v < (PUSHINTMAX+1):
				self.stack.append(str(v))
			else:
				print "Int "+str(v)+" too large to be pushed to stack."
		else:
			# if character (avoiding strings by using [0]
			self.stack.append(v[0])
			
	def toTop(self, v):
		"""
			Set variable to top of stack. Currently done by key value in stack
			(so you better know where your data is!) Potential work around but
			NYI.
		"""
		self.stack.insert(0, self.stack.pop(v))
		
	def pushTop(self, v):
		"""
			Push variable value to top of stack. See push.
		"""
		# since all we are doing is pushing to top instead of bottom,
		# we can reuse code from push()
		if isinstance(v,(int,long)):
			# if integer
			if v < (PUSHINTMAX+1):
				self.stack.insert(0, str(v))
			else:
				print "Int "+str(v)+" too large to be pushed to stack."
		else:
			# if character (avoiding strings by using [0]
			self.stack.insert(0, v[0])

	def newBuffer(self):
		"""
			Creates a new buffer
		"""
		# check for buffer
		if not self.bufferArray:
			self.bufferArray.append("00000")
		else:
			self.bufferArray.append("0000"+str(self.bufferCount))
		self.bufferCount += 1

	def selectBuffer(self, bufferName):
		self.currentBuffer = bufferName
		self.currentBufferData = {bufferName: ""}
		
	def printBuffer(self):
		b = self.currentBuffer
		if not b:
			print "Cannot print. No buffer selected."
		else:
			print self.currentBufferData[b]
			
	def readInput(self):
		usrIn = raw_input()
		self.currentBufferData[self.currentBuffer] = usrIn

# debugging stuff
x = SfCommands()
x.newBuffer()
x.newBuffer()
for c in "hello":
	x.push(c)
	
x.toTop(3)
print x.stack

x.selectBuffer("00001")
for y in x.stack:
	x.currentBufferData[x.currentBuffer] += (y)
x.printBuffer()
x.selectBuffer("00000")
x.readInput()
x.printBuffer()