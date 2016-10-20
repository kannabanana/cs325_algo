import os;
import sys;
import re;
import math;

def read_num(idx, length):
	fo = open(sys.argv[1], "r")
	if idx % 2 == 0:
		for i in range(0,idx): #get correct line
			tmp = fo.readline().split('),')
		print(tmp)
		for i in range(0,len(tmp)):
			tmp[i] = tmp[i][1:] #slice first char, open paren 
			test = tmp[i].split(',');
			print("test=%s" % (test))
		
		return tmp
	else: #line is singular number
		for i in range(0,idx):
			tmp = fo.readline();
		return int(tmp)

def main():
	#huge enormous sloppy arg stuff
#	fo = open(sys.argv[1], "r")
#	M = fo.readline();
#	M = int(M)
#	print("m=%s" % (M))
#	P = [[0 for x in range(2)] for y in range(M)]
#	tmp = fo.readline().split('),')
#	for i in range(0,len(tmp)):
#		tmp[i] = tmp[i][1:]
#		for j in range(0,len(tmp[i])):
#			if j == 0:
#				P[i][0] = int(tmp[i][j])
#			if j == 2:
#				P[i][1] = int(tmp[i][j])
#	print(P)	
#	N = fo.readline();
#	N = int(N)
#	print("n=%s" % (N))
#	Q = [[0 for x in range(2)] for y in range(N)]
#	tmp = fo.readline().split('),')
#	for i in range(0,len(tmp)):
#		tmp[i] = tmp[i][1:]
#		for j in range(0,len(tmp[i])):
#			if j == 0:
#				Q[i][0] = int(tmp[i][j])
#			if j == 2:
#				Q[i][1] = int(tmp[i][j])
#	print(Q)	
#	T = fo.readline();
#	T = int(T)
#	print("t=%s" % (T))
#	L = fo.readline().split(',')
#	for i in range(0,len(L)):
#		L[i] = int(L[i])
#	print(L)
#
#	#maybe make above its own function
#
	M = read_num(1,0);
	print(M);
	P = read_num(2,M);
	print(P);

main()
