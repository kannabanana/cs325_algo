#NAME: SR Kanna, Isaac Stallcup
#COURSE: Algorithms CS325
#DATE: Fall 2016, 10/23/2016
#INSTRUCTOR: Amir Nayyeri

import os;
import sys;
import re;
import math;
import random;



#read from file
def read_num(idx, length,text):
	fo = open(text, "r")
	A = [[0 for x in range(2)] for y in range (0,length)]

	#choose even line number, but not 6
	if idx % 2 == 0 and idx != 6:
		for i in range(0,idx): 						#get correct line
			tmp = fo.readline().split('),')
		for i in range(0,len(tmp)):
			tmp[i] = tmp[i][1:] 					#slice first char, open paren 
			test = tmp[i].split(',')
			test[len(test)-1] = test[len(test)-1].rstrip('()\n\r')
			A[i][0] = int(test[0])
			A[i][1] = int(test[1].strip(')\n'))
		return A

	elif idx == 6: 								#list of leash lengths
		B = [0 for x in range(0,length)]
		for i in range(0,idx):
			tmp = fo.readline().split(',');
		for i in range(0,length):
			B[i] = int(tmp[i].strip(')\n'))
		return B

	#odd numbers
	else: 									#line is singular number
		for i in range(0,idx):
			tmp = fo.readline();
		return int(tmp)



#recursive solution
def J(P,i,Q,j,l):

	if i >= len(P) and j >= len(Q):					 #if BOTH are finished, a path exists
		return True

	elif i >= len(P):						 #if one is finished but not other, then try another path
		return False

	elif j >= len(Q):
		return False

	#first check length, return False if length is more than l
	dist = math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))
	if math.ceil(dist) > l:
		return False

	if J(P,i+1,Q,j,l) == True:
		return True
	elif J(P,i,Q,j+1,l) == True:
		return True
	elif J(P,i+1,Q,j+1,l) == True:
		return True
	
	return False 							#if no possible path returns true




#dynamic programming solution
def DP(P,i,Q,j):

	if i >= len(P) and j >= len(Q):
		return 

	dist = math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))

	return dist+min(
		 DP(P,i+1,Q,j),						#min because you're trying to find the minimum leash length
	 	 DP(P,i,Q,j+1),
		 DP(P,i+1,Q,j+1)
		)


#print to text file
def output(num):
	fo = open("output.txt","w+")
	fo.write(str(num))


#main
def main():

	#types are all good!
#	print "M ", M, "type ",type(M)
#	print "P ",P, "type " ,type(P),P[1][0]
#	print "N ",N,"type " ,type(N)
#	print "Q ",Q,"type " , type(Q), type(Q[0])
#	print "T ",T,"type ", type(T)
#	print "L ",L,"type ",type(L), type (L[0])



	#read number takes line number from input.txt, num/list and file to read from
	M = read_num(1,0,sys.argv[1]);
	P = [[0 for x in range(2)] for y in range(0,M)]
	P = read_num(2,M,sys.argv[1]);				


	N = read_num(3,0,sys.argv[1]);
	Q = [[0 for x in range(2)] for y in range(0,N)]
	Q = read_num(4,N,sys.argv[1]);

	T = read_num(5,0,sys.argv[1]);
	L = read_num(6,T,sys.argv[1]);
	L.sort()				#sort the leases in increasing order


	#get the smallest possible leash
	val = DP(P,0,Q,0)


	#check the best possible match in the function
		

	#sorted
	#check if it's the value
	#if it's bigger than the value, then it's the new value
	print "the original value is ", val
	for x in range(0,len(L)):
		if L[x] == val:
			break	
		elif L[x] > val:
			val = L[x]
			break
	output(val)		#write to output.txt the leash length

main()
