import os;
import sys;
import re;
import math;
import random;

def read_num(idx, length, text):
	#read input.txt
        fo = open(text, "r")
	A = [[0 for x in range(2)] for y in range (0,length)] #storage array
        #idx is the line number of input.txt to read; if it's divisible by 2,
        #then it is the set of P points, Q points or leashes and is treated so
        if idx % 2 == 0 and idx != 6: #if we're reading P points or Q points
		for i in range(0,idx): #get correct line
			tmp = fo.readline().split('),') #split on ), to 
                                                        #seperate points out
		for i in range(0,len(tmp)):
			tmp[i] = tmp[i][1:] #slice first char (always an 
                        #open paren since we've sliced on ), earlier) 
			test = tmp[i].split(',')#test is the xy tuple for points
			test[len(test)-1] = test[len(test)-1].rstrip('()\n\r')
                        #strip newline characters, any sneaky parens
			A[i][0] = int(test[0]) #x-coord
			A[i][1] = int(test[1].strip(')\n')) #y-coord
		return A #return 2-d array of points
		#FUCK YEAH INTERPRETED LANGUAGES NOT REQUING
                #SPECIFIED RETURN TYPE!
	elif idx == 6: #list of leash lengths
		B = [0 for x in range(0,length)]
		for i in range(0,idx):
			tmp = fo.readline().split(',');
		for i in range(0,length):
			B[i] = int(tmp[i].strip(')\n'))
		return B
		
	else: #line is singular number
		for i in range(0,idx):
			tmp = fo.readline();
		return int(tmp)

#function J
#inputs:
#   P - 2-d array of points of form (x,y)
#   i - index for current element of P
#   Q - 2-d array of points of form (x.y)
#   j - index for current element of Q
#   l - current leash length compared against

#This function examines whether or not the distance between
#points P[i] and Q[j] is greater than the given leash
#length. If so, it returns False. It returns True when the
#end of BOTH arrays has been reached without finding a
#distance greater than the leash length.

def J(P,i,Q,j,l):
	if i >= len(P) and j >= len(Q): 
            #if BOTH are finished, a path exists
            #with leash length l, so we return True
		return True
	elif i >= len(P): #if one is finished but not other, then 
                          #try another path
		return False
	elif j >= len(Q):
		return False

        #standard Pythagoras
	dist = math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))
	if math.ceil(dist) > l:
		return False
            #if distance between two points we want is > l, return False

        #recursive calls: try first increasing P, then Q, then both
	if J(P,i+1,Q,j,l) == True:
		return True
	elif J(P,i,Q,j+1,l) == True:
		return True
	elif J(P,i+1,Q,j+1,l) == True:
		return True
	
	return False #if no possible path returns true

def output(num):
	fo = open("output.txt","w+")
	fo.write(str(num))

def main():
        #set recursion limit to accept very large test cases, like #5
        sys.setrecursionlimit(10000)	

        #read in data from input.txt    
        M = read_num(1,0,"input.txt");
	P = [[0 for x in range(2)] for y in range(0,M)]
	P = read_num(2,M,"input.txt");
	N = read_num(3,0,"input.txt");
	Q = [[0 for x in range(2)] for y in range(0,N)]
	Q = read_num(4,N,"input.txt");
	T = read_num(5,0,"input.txt");
	L = read_num(6,T,"input.txt");
        #L is sorted, becuase we find the shortest viable leash
        #by looping over all leashes, and if they are sorted
        #the first one that works is the shortest viable leash.
        L.sort()
	
        #loop over the list of leashes, trying each
        val = 0
	for x in range(0,T):
		val = J(P,0,Q,0,L[x])
		if val == True:#if we find one that works
			val = L[x] #remember the value
			break
        output(val)	#ouput to output.txt


main()
