#NAME: SR Kanna, Isaac Stallcup
#COURSE: Algorithms CS325
#DATE: Fall 2016, 10/11/2016
#INSTRUCTOR: Amir Nayyeri
#PURPOSE: intersectCount.py is a program to count the number of intersections recursively for cs325

import random;
import os;
import sys;


#gets vector Q, P from whatever input text we give it
def input_list(text):
	fo = open(text,"r")
#	print fo.read()			prints out all contents in the file
	master = [10,15,20];
	master[0] = fo.readline()
#	print "The number of line segments is", master[0]
	master[1] = fo.readline()
#	print "P is ", master[1]
	master[2] = fo.readline()
#	print "Q is ", master[2]
	return master

#def n2(Q,P,N, intersection):
	

#test function - wanted to see how python handled functions and lists
def print_list(Q):
	print "The list is", Q
	return



def n2(P,Q,N,intersection):
#	print "inside n2 ",
#	print "N is ", N
#	print " P is",P
#	print "Q is ",Q
#	print "intersection is ", intersection

	if N == 0:
		print "base case!"
		return
	else:
		print "not base case!"
		for i in range(0,N):
		#Q(i) > Q(N) and P(i) < P(N)		
			if(Q[i] > Q[N]):
				if(P[i] < P[N]):
					print "going to update intersection"
					++intersection;
		return n2(P,Q,N-1,intersection);



#define main
def main():
	intersection = 0;
	temp = [0,10,15];

	#input list P,Q and number of line segments from a given text file
	temp = input_list(sys.argv[1]);	

	#assign them to values
	N = temp[0];
	P = temp[1];
	Q = temp[2];	
	

#n2 algorithm
	n2(P,Q,N,intersection);
#	print "The number of intersections is ", intersection
#call main
main()
