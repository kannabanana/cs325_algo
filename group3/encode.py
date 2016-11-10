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

#Input function
def getipt():
    fo = open("input.txt","r")
    parse = fo.readline();
    print(parse)
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
                print("%s, %s" % (C[j],key1[j]))
                list1.append(key1[j])


def out2(C,F,key1,ipt,freqlist):
    for i in range(0,len(C)):
        freqlist.append(key1[i])
        freqlist.append(format(F[i],'019b'))


def out3(C,F,key2):


#huffman_algorithm
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
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
 

def main():
    C = []
    F = []
    key1 = []
    key2 = []
    list1 = []
    freqlist = []
    ipt = getipt()

    getlists(C,F,ipt)

    out1(C,F,key1,ipt,list1)
    str1 = ''.join(list1)
    print(str1)
    print("output1: %s" % (len(str1)))

    out2(C,F,key1,ipt,freqlist)
    str2 = ''.join(freqlist)
    print(str2)
    print("output2: %s" % (len(str2)))


    

    out3(C,F,key2)

main()