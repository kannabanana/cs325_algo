#SR Kanna
#Course: Intro to Security
#HW1

#bloom filters in python

import random;
import os;
import sys;
import re;
import hashlib

#generates random list of values of size 10
def salt_fun(salt,num):
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for x in range(0,num):
		i = random.randint(0,25)
		salt[x] = alpha[i]	
	return salt

def output(salt,text):
	fo = open(text,"a")		#will create output.txt if it doesn't exist
	fo.write(salt)


def main():
	i = sys.argv[1]
	i = int(i)
	salt = ['a']*i
	salt = salt_fun(salt,i)
	str1 = ''.join(salt)
	output(str1,sys.argv[2])

main()
