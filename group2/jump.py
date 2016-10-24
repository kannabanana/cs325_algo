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


def memoJ(P,i,Q,j,l,memo):
	for k in range(0,len(memo)):
		if memo[k] == [i, j]:
			print("gotem")
			return False
	
	if i >= len(P) and j >= len(Q):
		return True
	elif i >= len(P):#P is finished, not Q
		return False  #go back and check the rest
	elif j >= len(Q):#same with Q finished not P
		return False

	
	dist = int(math.ceil(math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))))
	print("dist=%s" % (dist))
	if dist > l:
		memo.append([i,j])
		print("memo=%s" % (memo))
		return False

	if memoJ(P,i+1,Q,j,l,memo) == True:
		return True
	if memoJ(P,i,Q,j+1,l,memo) == True:
		return True
	if memoJ(P,i+1,Q,j+1,l,memo) == True:
		return True

	return False

def dynamicJ(P,i,Q,j,l):
	print("DYANAMICJ: I=%s J=%s" % (i,j))
	#base cases: if we're at the end, return the shortest path value.
	if i >= len(P) and j >= len(Q):
		return True
	elif i >= len(P):#P is finished, not Q
		return False  #go back and check the rest
	elif j >= len(Q):#same with Q finished not P
		return False

	#calculate distance between two given points
	dist = math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2))
	print("distance between (%s,%s) and (%s,%s)=%s" % (P[i][0],P[i][1],Q[j][0],Q[j][1],dist))
	intcdist = int(math.ceil(dist))
	print("itegered and ceilinged distance is %s" % (intcdist)) 

	if intcdist > shortest:
		print("distance is > shortest distance so far, %s" % (shortest))
		return False
	else:
		print("@@@@ replacing shortest distance with %s" % (intcdist))
		shortest = intcdist

	valB = dynamicJ(P,i+1,Q,j+1,shortest)
	print("result of dynamicJ with both jump = %s" % (valB))
	if valB == True:
		return True
	valP = dynamicJ(P,i+1,Q,j,shortest)
	print("result of dynamicJ with P jump = %s" % (valP))
	if valP == True:
		return True
	valQ = dynamicJ(P,i,Q,j+1,shortest)
	print("result of dynamicJ with Q jump = %s" % (valQ))
	if valQ == True:
		return True
	print("comparing %s %s %s %s" % (shortest, valP, valQ, valB))

	return False

#	print("dynamicJ; i=%s j=%s" % (i, j))
	#normal memoization is just keeping track of shortest, not returning minimum
#	print("shortest=%s" % (shortest))
#	if i >= len(P) and j >= len(Q): #if BOTH are finished, a path exists
#		return shortest
#	elif i >= len(P): #if one is finished but not other, then try another path
#		return 2380 
#	elif j >= len(Q):
#		return 2380

#	print("PRE: shortest=%s" % (shortest))
#	dist = math.ceil(math.sqrt(pow((P[i][0]-Q[j][0]),2)+pow((P[i][1]-Q[j][1]),2)))
#	print("dist=%s" % (dist))
#	if (dist > shortest):
#		return shortest
#	jumpP = dynamicJ(P,i+1,Q,j,shortest)
#	print("jumpP=%s" % (jumpP))
#	jumpQ = dynamicJ(P,i,Q,j+1,shortest)
#	print("jumpQ=%s" % (jumpQ))
#	jumpB = dynamicJ(P,i+1,Q,j+1,shortest)
#	print("jumpB=%s" % (jumpB))

#	shortest = min([dist, jumpP, jumpQ, jumpB, shortest])
#	print("@@@@ POST: shortest=%s" % (shortest))
#	print("")
#	return shortest

def output(num):
	fo = open("output.txt","w+")
	fo.write(str(num))

def main():
	M = read_num(1,0,sys.argv[1]);
	P = [[0 for x in range(2)] for y in range(0,M)]
	P = read_num(2,M,sys.argv[1]);
	N = read_num(3,0,sys.argv[1]);
	Q = [[0 for x in range(2)] for y in range(0,N)]
	Q = read_num(4,N,sys.argv[1]);
	T = read_num(5,0,sys.argv[1]);
	L = read_num(6,T,sys.argv[1]);
	L.sort()
	
#	val = dynamicJ(P,0,Qi,0,2830) 
	#1000 maximum possible value, so maximum possible distance is
	#sqrt((-1000-1000)^2+(-1000+1000)^2)=2828. Algo will count
	#any path found as shorter than this making it a good starting point
#	print("overall shortest = %s" % (val))

	for x in range(0,T):
		print("memo")
		memo = []
		memoJ(P,0,Q,0,L[x],memo)

#	output(val)

main()
