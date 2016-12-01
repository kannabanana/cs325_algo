import random;
import os;
import sys;
import re;
from itertools import combinations;

def YES():
    fo = open("output.txt",'w')
    fo.write("YES")
    fo.close()

def NO():
    fo = open("output.txt",'w')
    fo.write("NO")
    fo.close()

def ipt():
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    edges = []
    for i in range(0,int(E)):
        edges.append((int(roads[i]),int(roads[i+1])))
        roads.pop(i+1)
    return [int(V),edges]

def find_crossings(edges):
    inters = []
    for x in range(0,len(edges)):
        for y in range(0,x):
            if edges[x][0] >= edges[y][1]:
                continue
            if edges[y][0] > edges[x][0] and edges[y][1] > edges[x][1]:
                inters.append((edges[x],edges[y]))
            if edges[y][0] < edges[x][0] and edges[y][1] < edges[x][1]:
                inters.append((edges[x],edges[y]))

    return inters

def evaluate(cnf,form):
    for n in cnf:
        if n[0][1] == form[n[0][0]]:
            continue
        elif n[1][1] == form[n[1][0]]:
            continue
        else:
            return False
    return True

def main():
    [V,edges] = ipt()
    key = [i for i in range(0,len(edges))]
    edges2alpha = dict(zip(edges,key))
    inters = find_crossings(edges)

    alpha = []
    for i in inters:
        alpha.append([edges2alpha[i[0]],edges2alpha[i[1]]])
    cnf = []
    for i in alpha:
        cnf.append([[i[0],True],[i[1],True]])
        cnf.append([[i[0],False],[i[1],False]])

    form = dict(zip(key,['' for n in key]))

    for i in range(0,len(key)+1):
        bools = list(combinations(key,i))
        for x in bools:
            for z in key:
                form[z] = True
            for y in x:
                form[y] = False
            if evaluate(cnf,form) == True:
                YES()
                return
    NO()
    return

main()
