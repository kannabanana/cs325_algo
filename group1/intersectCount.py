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


#gets vector Q, P from whatever input text we give it
def input_listQ(text):
	fo = open(text,"r")
	master = [10,15,20];
	master[0] = fo.readline()
	master[1] = fo.readline()

	master[2] = fo.readline()

	Q = master[2].split(",") 
	return Q


#test function - wanted to see how python handled functions and lists
def print_list(Q):
	print "The list is", Q
	return


#n2 algorithm (compares Q[i] > Q[n] && P[i] < P[n])
def n2(P,Q,N,intersection):
#	print "inside n2 ",
#	print "N is ", N
#	print " P is",P
#	print "Q is ",Q
#	print "intersection is ", intersection

	if N == 0:
#		print "base case! Intersection count is", intersection 
		return intersection;
	else:
#		print "not base case!"
		for i in range(0,N):
		#Q(i) > Q(N) and P(i) < P(N)		
			if(Q[i] > Q[N]):
#				print "Q[i] is ",Q[i],"Q[N] is ", Q[N]
				if(P[i] < P[N]):
#					print "P[i] is ", P[i],"P[N] is ",P[N]
#					print "going to update intersection from", intersection
					#++intersection; omg python doesn't let me do this
					intersection += 1;
#					print "intersection is now", intersection
		return n2(P,Q,N-1,intersection);





#combine the two arrays
def combine(first,second):

	fo = open("output.txt","r")
	nlogn_intersection = fo.readline()

	temp = []		#empty list

	#the first and second can't be zero
	while len(first) != 0 and len(second) != 0:
		if first[0] < second[0]:
			temp.append(first[0])
			first.remove(first[0])
		else:
			temp.append(second[0])
			second.remove(second[0])
	if len(first) == 0:
		temp += second
	else:
		temp += first
    
	return temp



#main function for mergesort
def mergesort(Q):


	#base case - length 0 or 1
	if len(Q) == 1 or len(Q) == 0:
   #     	return nlogn_intersection
		return Q
    	
	else:
		print "\n\n"
		print "starting mergesort, Q=",Q
		mid = len(Q)/2			#divide by two
		i = 0;
		print "i=",i
		print "mid=",mid
		j = mid+1;
		z = mid;
		print "j=",j
#following the algorithm - lets see what happens (follow the yellow brick road)
		for k in range(0,mid):
			print ("i=%s z=%s j=%s" % (i, z, j))
			print ("Qi=%s Qz=%s" % (Q[i], Q[z]))
			if Q[i] > Q[z]:
				print "INTER FOUND!!!!!!!!!!!!!!!!!!!!!!!!"
				i += 1;
			elif j>mid:
				i += 1;
			
				fo = open("output.txt","r")
				nlogn_intersection = fo.readline()
		
				nlogn_intersection = int(nlogn_intersection)
				nlogn_intersection += 1;
				print "num_inter NOW SET TO:           ",nlogn_intersection

				output(nlogn_intersection)
				

			elif i>mid:
				j += 1;
				print "wierd case"
				

#LOL this case never hits
			elif Q[i] < Q[j]:

				i += 1;
				fo = open("output.txt","r")
				nlogn_intersection = fo.readline()

				print "SECOND CASE nlogn_intersection is ",nlogn_intersection
				nlogn_intersection = int(nlogn_intersection)	
				nlogn_intersection += 1;
				print "updated nlogn_intersection is ",nlogn_intersection
				output(nlogn_intersection)

			else:
				j +=1;
				print "fall through case"

       		first = mergesort(Q[:mid])	#recursive call on the mid
        	second = mergesort(Q[mid:])
        	return combine(first,second)



#function to output to output.txt
def output(intersection):
#	print "in output the intersetemption is ", intersection
	fo = open("output.txt","w+")		#will create output.txt if it doesn't exist
	fo.write(str(intersection))



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
#	intersection = n2(P,Q,N-1,intersection);	
	#write to output function
#	output(intersection);

	nlogn_intersection = 0	
	output(nlogn_intersection);

	Q = mergesort(Q);
	print Q


#call main
main()
