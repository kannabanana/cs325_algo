import random;
import os;
import sys;
import re;

def eval_clauses(clause):
    #if a single clause is not false, return true
    neg = []
    pos = []
    clause = clause.split('&')
    for l in clause:
        if l[0] == '!':
            neg.append(l[1])
        else:
            pos.append(l)
    inter = set(pos) & set(neg)
    for p in pos:
        for n in neg:
            if p == n:
                return False
    for n in neg:
        for p in pos:
            if p == n:
                return False
    return True



def ipt_list():
    fo = open("input.txt")
    form = fo.readline().split('|')
    return form

def main():
    form = ipt_list()
    for clause in form:
        if eval_clauses(clause) == True:
            print "TRUE"
            return
    print "FALSE"
    return

main()
