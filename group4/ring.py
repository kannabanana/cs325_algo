import random;
import sys;
import os;
import re;

class Graph:
    def __init__(self,V,vertices,roads):
        self.adj = dict(zip(vertices,[[] for x in vertices]))
        self.roadmap = dict(zip(range(1,1+len(roads)),roads))
        
    def add_edge(self,to,fr):
        self.adj[fr].append(to)

    adj = dict()
    roadmap = dict()

def ipt():
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    for i in range(0,int(E)):
        #replace with tuples if things get tricky with access
        roads[i] = '('+roads[i] +','+ roads[i+1]+')'
        roads.pop(i+1)
    vertices = []
    #roads are numbered; negations of roads are negative #s
    for x in range(1,1+len(roads)):
        vertices.append(x)
        vertices.append(-x)
    return [int(V),int(E),roads,vertices]

def main():
    [V,E,roads,vertices] = ipt()
    G = Graph(V,vertices,roads)
    print G.roadmap
    print G.adj
    


main()
