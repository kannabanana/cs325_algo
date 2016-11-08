import os;
import sys;
import re;
import string;
from string import ascii_lowercase;

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
    for i in ipt:
        for j in range(0,len(C)):
            if C[j]==i:
                print("%s, %s" % (C[j],key1[j]))
                list1.append(key1[j])

def out2(C,F,key1,ipt,freqlist):
    for i in range(0,len(C)):
        freqlist.append(key1[i])
        freqlist.append(format(F[i],'019b'))

def main():
    C = []
    F = []
    key1 = []
    ipt = getipt()
    getlists(C,F,ipt)
    for i in range(0,len(C)):
        key1.append(format(i, '05b'))
    list1 = []
    freqlist = []
    out1(C,F,key1,ipt,list1)
    str1 = ''.join(list1)
    print(str1)
    print("output1: %s" % (len(str1)))

    out2(C,F,key1,ipt,freqlist)
    print(freqlist)
    str2 = ''.join(freqlist)
    print("output2: %s" % (len(str2)))

main()
