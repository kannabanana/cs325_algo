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


def output(num):
	fo = open("output.txt","w+")
	fo.write(str(num))

def main():
	M = read_num(1,0,sys.argv[1]);
	#print("m=%s" % (M))
	P = [[0 for x in range(2)] for y in range(0,M)]
	P = read_num(2,M,sys.argv[1]);
	#print("P=%s" % (P))
	N = read_num(3,0,sys.argv[1]);
	#print("n=%s" % (N))
	Q = [[0 for x in range(2)] for y in range(0,N)]
	Q = read_num(4,N,sys.argv[1]);
	#print("Q=%s" % (Q))
	T = read_num(5,0,sys.argv[1]);
	#print("t=%s" % (T))
	L = read_num(6,T,sys.argv[1]);
	L.sort()
	#print("L=%s" % (L))

	for i in range(0,T):
		#print("i=%s" % (i))
		val = J(P,0,Q,0,L[i])
		#print("%s=%s" % (L[i], val))
		if val == True:
			output(L[i])
			break

main()
