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
	#check the coordinate and everything before it
	for i in range(0,len(roads),2):
		for x in range(0,i,2):
			if(roads[x] >= roads[i] and roads[x+1] < roads[i+1]):
					print "the first coordinates are ", roads[x],roads[x+1],"the second ones are ",roads[i],roads[i+1]
		#it's been "inserted"
		#check if it clashes with anything before it
			#check that by checking every coordinated inserted before
				#clash occurs if the first one is equal or less than AND the second is bigger

def main():
	[V,E,roads] = input()
	print roads
	check_cross(roads)
main()
