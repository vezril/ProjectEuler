#!/usr/bin/env python

class fib:
	def __init__(self):
		self.n1 = 1
		self.n = 2
		self.f = 3
		
	def NextN(self):
		self.tmp = self.n1 + self.n
		self.n1 = self.n
		self.n = self.tmp
		self.f = self.f + 1
		
	def GetF(self):
		return self.f
		
	def GetN(self):
		return self.n
	
	def GetN1(self):
		return self.n1
		
	def PrintAll(self):
		print 'F: ' + str(self.GetF())
		print 'N: ' + str(self.GetN())
		print 'N1: ' + str(self.GetN1())
		print ''
		
f = fib()

while True:
	if len(str(f.GetN())) > 1000:
		f.PrintAll()
		break
	f.NextN()