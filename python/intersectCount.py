#NAME: SR Kanna, Isaac Stallcup
#COURSE: Algorithms CS325
#DATE: Fall 2016, 10/11/2016
#INSTRUCTOR: Amir Nayyeri
#PURPOSE: intersectCount.py is a program to count the number of intersections recursively for cs325

import random;
import os;
import sys;
import re;


#gets vector Q, P from whatever input text we give it
def input_listN(text):
	fo = open(text,"r")
#	print fo.read()			prints out all contents in the file
	N = 0;
	N = fo.readline()
	return N; 


#gets vector Q, P from whatever input text we give it
def input_listP(text):
	fo = open(text,"r")
#	print fo.read()			prints out all contents in the file
	master = [10,15,20];
	master[0] = fo.readline()
#	print "The number of line segments is", master[0]

	master[1] = fo.readline()
	P = master[1].split(",") 
	return P



def input_listQ(text):
	fo = open(text,"r")
	master = [10,15,20];
	master[0] = fo.readline()
	master[1] = fo.readline()

	master[2] = fo.readline()

	Q = master[2].split(",") 
	return Q

#def n2(Q,P,N, intersection):
	

#test function - wanted to see how python handled functions and lists
def print_list(Q):
	print "The list is", Q
	return



def n2(P,Q,N,intersection):
	print "inside n2 ",
	print "N is ", N
	print " P is",P
	print "Q is ",Q
	print "intersection is ", intersection

	if N == 0:
		print "base case! Intersection count is", intersection 
		return intersection;
	else:
		print "not base case!"
		for i in range(0,N):
		#Q(i) > Q(N) and P(i) < P(N)		
			if(Q[i] > Q[N]):
				print "Q[i] is ",Q[i],"Q[N] is ", Q[N]
				if(P[i] < P[N]):
					print "P[i] is ", P[i],"P[N] is ",P[N]
					print "going to update intersection from", intersection
					#++intersection; omg python doesn't let me do this
					intersection += 1;
					print "intersection is now", intersection
		return n2(P,Q,N-1,intersection);



#define main
def main():
	intersection = 0;

	#input list P,Q and number of line segments from a given text file
	N = input_listN(sys.argv[1]);	
	N = int(N)	#convert str to int


	#getting the P list without commas
	P = input_listP(sys.argv[1]);
	for i in range(0,len(P)):
		P[i] = int(P[i])
	
	#getting the Q list without commas (cheating because only one return and I know how many lines in text file)
	Q = input_listQ(sys.argv[1]);	
	for i in range(0,len(Q)):
		Q[i] = int(Q[i])


	
	#n2 algorithm
#	intersection = n2(P,Q,N*2,intersection);
#	print "The number of intersections is ", intersection
#call main
main()
