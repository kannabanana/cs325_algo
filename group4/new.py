import random;
import os;
import sys;
import re;

class Graph:
    def __init__(self,V,edges):
        #takes in # vertices, list of all edges
        self.V = V
        #adjacency list for graph
        self.adj = dict(zip([i for i in range(0,V)],[[] for i in range(0,V)]))
        for x in edges:
            self.adj[x[0]].append(x[1])
            self.adj[x[1]].append(x[0])

    V = 0
    adj = dict()

def ipt(): 
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    edges = []
    for i in range(0,int(E)):
        edges.append((int(roads[i]),int(roads[i+1])))
        roads.pop(i+1)
    return [int(V),edges]

def main():
    [V,edges] = ipt()
    G = Graph(V,edges)
    print G.adj


main()
