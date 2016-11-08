import os;
import sys;
import re;
import math;
import random;

def read_num(idx, length,text):
	fo = open(text, "r")
	A = [[0 for x in range(2)] for y in range (0,length)]
	#print("len=%s" % (length))
	if idx % 2 == 0 and idx != 6:
		for i in range(0,idx): #get correct line
			tmp = fo.readline().split('),')
#		print(tmp)
		for i in range(0,len(tmp)):
#			print(tmp[i])
			tmp[i] = tmp[i][1:] #slice first char, open paren 
			test = tmp[i].split(',')
			test[len(test)-1] = test[len(test)-1].rstrip('()\n\r')
			#print(test)
#			print("i=%s test=%s" % (i,test))
#			print(len(A))
#			print(A[i][0])
			A[i][0] = int(test[0])
			A[i][1] = int(test[1].strip(')\n'))
		return A
		#FUCK YEAH INTERPRETED LANGUAGES NOT REQUING SPECIFIED RETURN TYPE!
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

def J(P,i,Q,j,l):
	#print("J with P=%s i=%s Q=%s j=%s l=%s" % (P,i,Q,j,l))
	if i >= len(P) and j >= len(Q): #if BOTH are finished, a path exists
		#print("reached end without violating conditions")
		return True
	elif i >= len(P): #if one is finished but not other, then try another path
		return False
	elif j >= len(Q):
		return False
	#print("ok")	
	#first check length, return False if length is more than l
	dist = math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))
	#print("dist between P[%s] and Q[%s] = %s" % (i, j, dist))
	#print("compare to l=%s" % (l))
	if math.ceil(dist) > l:
		#print("dist %s > l %s" % (dist, l))
		return False

	if J(P,i+1,Q,j,l) == True:
		return True
	elif J(P,i,Q,j+1,l) == True:
		return True
	elif J(P,i+1,Q,j+1,l) == True:
		return True
	
	return False #if no possible path returns true


def memoJ(P,i,Q,j,L):
	if i >= len(P) and j >= len(Q): #if BOTH are finished, a path exists
		#print("reached end without violating conditions")
		return True
  	
#	print("@@ i=%s j=%s" % (i,j))
#	print("L currently %s" % (L))
	dist = int(math.ceil(math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))))
#	print("dist=%s" % (dist))
	initLen = len(L)
	for x in range(0,len(L)):
		if L[x] >= dist:
		    break
	for y in range(0,x):
	    L.pop(y)
#	print(L)	
	#figure out which of next 3 steps is shortest, take it
	
        val = []
        if i+1 < len(P):
            val.append(int(math.ceil(math.sqrt(pow((P[i+1][0]-Q[j][0]),2)+pow((P[i+1][1]-Q[j][1]),2)))))
        else:
            val.append(sys.maxint)
        if j+1 < len(Q):
            val.append(int(math.ceil(math.sqrt(pow((P[i][0]-Q[j+1][0]),2)+pow((P[i][1]-Q[j+1][1]),2)))))
        else:
            val.append(sys.maxint)
        if j+1 < len(Q) and i+1 < len(P):
            val.append(int(math.ceil(math.sqrt(pow((P[i+1][0]-Q[j+1][0]),2)+pow((P[i+1][1]-Q[j+1][1]),2)))))
        else:
            val.append(sys.maxint)
#	print(val)
        
        if min(val) == sys.maxint:
            return True
        if min(val) == val[0]:
 #           print("val[0] = %s shortest" % (val[0]))
            memoJ(P,i+1,Q,j,L)
        elif min(val) == val[1]:
  #          print("val[1] = %s shortest" % (val[1]))
            memoJ(P,i,Q,j+1,L)
        elif min(val) == val[2]:
   #         print("val[2] = %s shortest" % (val[2]))
            memoJ(P,i+1,Q,j+1,L)
        
        return False

def output(num):
	fo = open("output.txt","w+")
	fo.write(str(num))

def main():
	M = read_num(1,0,"input.txt");
	P = [[0 for x in range(2)] for y in range(0,M)]
	P = read_num(2,M,"input.txt");
	N = read_num(3,0,"input.txt");
	Q = [[0 for x in range(2)] for y in range(0,N)]
	Q = read_num(4,N,"input.txt");
	T = read_num(5,0,"input.txt");
	L = read_num(6,T,"input.txt");
	L.sort()
	

	val = 0
	memoJ(P,0,Q,0,L)
        val = L[0]
        output(val)
#	if M < 500 and N < 500 and T < 500:
#		for x in range(0,T):
#			val = J(P,0,Q,0,L[x])
#			if val == True:
#				val = L[x]
#				break
#		print("normal iterative found %s" % (val))
#	else:
#		print("too big for normal recursion! silly python.")
#		memo = []
#		val = memoJ(P,0,Q,0,L,memo)
#		print("memoized version found %s" % (val))
	


main()
