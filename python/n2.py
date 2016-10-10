#s is a n2 program to count the number of intersections recursively for cs325
#random function in python
import random;
import os;
import sys;


#gets vector Q, P from whatever input text we give it
def input_list(P,Q,N,text):
	fo = open(text,"r")
#	print fo.read()			prints out all contents in the file
	n = fo.readline()
	print "The number of line segments is", n
	P = fo.readline()
	print "P is ", P
	Q = fo.readline()
	print "Q is ", Q
	return

#def n2(Q,P,N, intersection):
	

#test function - wanted to see how python handled functions and lists
def print_list(Q):
	print "Q is", Q
	return


def n2(P,Q,N,intersection):
	for i in range(0,N):
		#Q(i) > Q(N) and P(i) < P(N)		
		if(Q[i] > Q[N]):
			if(P[i] < P[N]):
				++intersection;
	return n2(P,Q,N-1,intersection);


#define main
def main():
	Q = [10,2,3];
	P = [1,2,3];
	N = 0;
	intersection = 0;

	#input list P,Q and number of line segments from a given text file
	input_list(P,Q,N,sys.argv[1]);	

#n2 algorithm
#	n2(P,Q,N,intersection);

#call main
main()
