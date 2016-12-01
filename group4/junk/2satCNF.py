import random;
import os;
import sys;
import re;

class Graph:
    def __init__(self,numVertices):
        self.keys = []
        for i in range(1,numVertices+1):
            self.keys.append(i)
            self.keys.append(-i)
        self.nbrs = dict(zip(self.keys,[[] for x in self.keys]))
        self.parents = dict(zip(self.keys,[[] for x in self.keys]))

    def add_edge(self,fr,to):
        self.nbrs[fr].append(to)
        self.parents[to].append(fr)
    

    keys = []
    nbrs = []
    parents = []

def neg(n):
    if n < 0:
        return abs(n)
    else:
        return -1*n

def ipt_list():
    fo = open("input.txt")
    [V,E] = fo.readline().rstrip().split(',')
    form = fo.readline().split('&')
    return [int(V),int(E),form]

def DFS(G,x,visited):
    print visited
    if x in visited:
        return
    visited.append(x)
    for y in G.nbrs[x]:
        if y in visited:
            continue
        else:
            DFS(G,y,visited)

def Kosaraju(G):
    #return 
    print G.nbrs
    print G.parents
    c = 0
    labeled = []
    vals_L = []
    visited = []
    for x in G.keys:
        if x in labeled:
            continue
        DFS(G,x,visited)
        c = c + 1
        labeled.append(x)
        vals_L.append(c)
    print labeled
    print vals_L
    labeled.reverse()
    vals_L.reverse()
    print labeled
    print vals_L

    rev = []
    for a in labeled:
        if a in rev:
            continue
        rev.append(a)

    


def main():
    [V,E,form] = ipt_list()
    print(form)

    G = Graph(V)

    for clause in form:
        print clause.split('|')
        bits = clause.split('|')
        bits = [int(x) for x in bits]
        G.add_edge(neg(bits[0]),bits[1])
        G.add_edge(neg(bits[1]),bits[0])

    print(G.nbrs)

    Kosaraju(G)
    
    return

main()
