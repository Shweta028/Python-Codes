#!/usr/bin/python2

#using simple functions with different types

#To perform simple addition of any type

def add(a,b):
	return (a+b)

#To append a variable value to another

def append(a,b):
	return str(a)+str(b)


#To repeat value of a parameter a number of times

def replicate(a,b):
	return (str(a)*b)

#To make a tuple with dynamic size and type

def make_tuple(*a):
	return a

#To add multiple values together

def add_multiple(*a):
	sum =0
	for i in a: sum=sum+i
	return sum

'''
print add(2,5)
print append("Shweta","Rajani")
print replicate("Shweta",5)
print make_tuple(3,4,5,6,7)
print add_multiple(1,2,3,4,5)
'''


