#s is a n2 program to count the number of intersections recursively for cs325
#random function in python
import random;
import os;
import sys;

#print the list
def print_list(Q):
	print "Q is", Q
	return


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



#define main
def main():
	Q = [10,15,20];
	P = [1,2,4];
	N = 0;

#	print_list(Q);		#print list
	input_list(P,Q,N,sys.argv[1]);	


#call main
main()
