"""
SR Kanna, Isaac Stallcup
Amir Nayyeri
CS325
Nov 29th 2016
"""



import random
import os
import string


#gets input from files
def input():
	fo = open("input.txt",'r')
	[V,N] = fo.readline().rstrip().split(',')  
	roads = fo.readline().split(',')
	return [int(V),int(N),roads]


#we know they cross IF 
#1	2	3	4	5#
#1		3
#1	2
	#2		4		VIOLATES THE RULE!!


#function checks if there are crosses
def check_cross(roads):
	l = len(roads)		#some even length number
	for x in range(0,l):
		for i in range(0,x):
			


def main():
	[V,E,roads] = input()
	print V
	print roads
	print len(roads)
main()
