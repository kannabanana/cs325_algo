#s is a n2 program to count the number of intersections recursively for cs325
#random function in python
import random;
import os;
import sys;


#gets vector Q, P from whatever input text we give it
def input_list(text):
	fo = open(text,"r")
#	print fo.read()			prints out all contents in the file
	master = [10,15,20];
	master[0] = fo.readline()
	print "The number of line segments is", master[0]
	master[1] = fo.readline()
	print "P is ", master[1]
	master[2] = fo.readline()
	print "Q is ", master[2]
	return master

#def n2(Q,P,N, intersection):
	

#test function - wanted to see how python handled functions and lists
def print_list(Q):
	print "Q is", Q
	return




def n2(P,Q,N,intersection):
	print N
	print P
	print Q
#	if N == 0:
#		print "base case!"
#		return
#	else:
#		for i in range(0,N):
#		#Q(i) > Q(N) and P(i) < P(N)		
#			if(Q[i] > Q[N]):
#				if(P[i] < P[N]):
#					print "going to update intersection"
#					++intersection;
#		n2(P,Q,N-1,intersection);


#define main
def main():
	intersection = 0;
	temp = [0,10,15];

	#input list P,Q and number of line segments from a given text file
	temp = input_list(sys.argv[1]);	

	#assign them to values
	N = temp[0];
	Q = temp[1];
	P = temp[2];	
	

#n2 algorithm
#	n2(P,Q,N,intersection);
#	print "The number of intersections is ", intersection
#call main
main()
