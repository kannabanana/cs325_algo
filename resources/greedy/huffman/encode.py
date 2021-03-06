#SR Kanna, Isaac Stallcup
#Algorithms CS325
#GA3
#Date: November 9th 2016
#Description: Data compression via simple encoding, run length and huffman codes. Given an input string (a-z) less than 2^19, generate the encoded file length of all three methods.

import os;
import sys;
import re;
import string;
from string import ascii_lowercase;
from heapq import heappush, heappop, heapify
from collections import defaultdict
 
#Input function
def getipt():
    fo = open("input.txt","r")
    parse = fo.readline();
    fo.close()
    return parse


def getlists(C,F,ipt):
    for i in ascii_lowercase:
        if ipt.count(i) != 0:
            C.append(i)
            F.append(ipt.count(i))


def out1(C,F,key1,ipt,list1):
    for i in range(0,len(C)):
        key1.append(format(i, '05b'))
    for i in ipt:
        for j in range(0,len(C)):
            if C[j]==i:
                list1.append(key1[j])


def out2(C,F,key1,ipt,freqlist):
    num = 0
    if len(C) == 1:
        freqlist.append(key1[0])
        freqlist.append(format(len(ipt),'019b'))
        return
    for i in range(0,len(ipt)):
        if ipt[i] == ipt[i-1]: #consecutive characters same
            num = num + 1
        if ipt[i] != ipt[i-1]:
            freqlist.append(key1[C.index(ipt[i])])
            freqlist.append(format(num,'019b'))
            num = 0



#huffman_algorithm
def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 

#convert string to binary - huffman
def bin(str1):
    str2 = str1[::-1]
    x = 0
    binary = 0
    lengthstr2 = len(str2)
    for x in range(0,lengthstr2):
        if str2[x] == "1":
            temp = pow(2,x)	
	    binary = binary+temp
    return binary


def output(num1,num2,num3):
    fo = open("output.txt","w")
    fo.write(str(num1)+"\n")
    fo.close()
    fo = open("output.txt","a")
    fo.write(str(num2)+"\n")
    fo.write(str(num3))


def main():
	C = []
	F = []
	key1 = []
	key2 = []
	list1 = []
	freqlist = []
	ipt = getipt()
	print len(ipt)
	#print "the length of the input is ",len(ipt)
	getlists(C,F,ipt)


        out1(C,F,key1,ipt,list1)
        str1 = ''.join(list1)

	out2(C,F,key1,ipt,freqlist)
	str2 = ''.join(freqlist)

        if len(C) == 1: #only 1 char
            total = len(ipt);
	    output(len(str1),len(str2),total)
            return


     	txt = "".join(ipt)
	symb2freq = defaultdict(int)
	for ch in txt:
		symb2freq[ch] += 1
	huff = encode(symb2freq)
	
#	print "Symbol\tWeight\tHuffman Code"
#        for p in huff:
#            print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])

	total = 0
	for p in huff:
		binary = len(p[1])
		temp = symb2freq[p[0]]*binary
		total = temp+total
 
	output(len(str1),len(str2),total)
main()

