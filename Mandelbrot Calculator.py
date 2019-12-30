#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class complex:
	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary
	def __str__(self):
		return str(self.real) + ' + ' + str(self.imaginary) + 'i'
	def add(self, c):
		return complex(float(c.real) + float(self.real), float(c.imaginary)+float(self.imaginary))
	def multiply(self, c):
		r = self.real * c.real - (self.imaginary * c.imaginary)
		i = 2 * self.imaginary * c.real
		return complex(r, i)
	def magnitude(self):
		r = self.real * self.real
		r += self.imaginary * self.imaginary
		return math.sqrt(r)

def calculate_main(a, b):
	print ('========================================================================')
	print ('Equation\t\tValue\t\t\t\tMagnitude         ')
	print ('========================================================================')
	for i in range(1,9):
		c = calculate(a, b)
		a = c
		

def calculate(a, b):
	c = a.multiply(a) 
	c = c.add(b)
	print ('f(0) = \t\t' + c.__str__()+'\t\t\t\t'+ str(c.magnitude()))
	return c

def main():
	r = input ('Enter real ' )
	i = input ('Enter imaginary ')
	b = complex(r,i)
	a = complex (0.0,0.0)
	calculate_main(a, b)
	
main()
	


# In[ ]:




