import random;
import sys;
import os;
import re;

class Graph:
    def __init__(self,V,vertices):
        self.adj = dict(zip(vertices,[[] for x in vertices]))
        
    def readable(self):
        for x in self.adj:
            print("%s: %s" % (x, self.adj[x]))

    def add_edge(self,to,fr):
        self.adj[fr].append(to)

    def edge(self,tup,val):
        return ((tup[0],tup[1]),val)

    adj = dict()

def ipt():
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    #get roads as vertex pairs
    #roads will be list of form ['to,from', 'to,from',...]
    for i in range(0,int(E)):
        roads[i] = (int(roads[i]),int(roads[i+1]))
        roads.pop(i+1)
    vertices = []
    for x in roads:
        vertices.append((x,'T'))
        vertices.append((x,'F'))
    return [int(V),int(E),vertices]

def main():
    [V,E,vertices] = ipt()
    G = Graph(V,vertices)
    G.add_edge(G.edge([0,2],'T'),G.edge([0,3],'F'))
    G.readable()
    


main()
