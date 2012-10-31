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
		self.STACKSIZE = 1024
		self.PUSHINTMAX = 999
		self.bufferCount = 0
		self.currentBuffer = ""
		# list of buffers, not buffer data
		self.bufferArray = []
		self.stack = []

	def push(self, v):
		if isinstance(v,(int,long)):
			if v < (PUSHINTMAX+1):
				self.stack.append(str(v))
			else:
				print "Int "+str(v)+" too large to be pushed to stack."
		else:
			self.stack.append(v[0])

	def addBuffer(self):
		if not self.bufferArray:
			self.bufferArray.append("00000")
		else:
			self.bufferArray.append("0000"+str(self.bufferCount))
		self.bufferCount += 1

	def printBuffer(self):
		return 0
		
	def toTop(self, v):
		return 0

x = SfCommands()
x.addBuffer()
x.addBuffer()
for c in "hello":
	x.push(c)
	
x.toTop('l')
print x.stack