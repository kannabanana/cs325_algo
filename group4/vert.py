import random;
import sys;
import os;
import re;

class Graph:
    #constructor
    def __init__(self,V,E,roads):
        self.V = V
        self.E = E
        self.vertexRange = [i for i in range(0,V)]
        self.adj = dict(zip(self.vertexRange,[[] for x in range(0,V)]))
        self.rev = dict(zip(self.vertexRange,[[] for x in range(0,V)]))
        
    def add_edge(self,fr,to):
#        print("link from %s to %s" % (fr, to))
        self.adj[fr].append(to)
        self.rev[to].append(fr)

    #adjacency list for directed graph
    adj = dict()
    rev = dict()
    V = 0
    E = 0
    vertexRange = []

def ipt(): #gets input from file, indexes the roads
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    for i in range(0,int(E)):
        roads[i] = (int(roads[i]),int(roads[i+1]))
        roads.pop(i+1)
    return [int(V),int(E),roads]

def populate_edges(G,edges,roads):
    return False

def initialDFS(G,stack,visited,curr):
    if curr in visited:
        return
#    print("%s parent" % (curr))
    visited.append(curr)
    for x in G.adj[curr]:
#        print("%s child" % (x))
        initialDFS(G,stack,visited,x)
    stack.append(curr)

def reverseDFS(G,stack,visited,curr,tree):
    if curr in visited:
        return
    if curr not in visited:
#        print("%s = curr" % (curr))
        visited.append(curr)
        tree.append(curr)
        for t in G.rev[curr]:
            reverseDFS(G,stack,visited,t,tree)

def Kosaraju(G):
    visited = []
    stack = []
    for x in G.vertexRange:
#        print("chose %s" % (x))
        initialDFS(G,stack,visited,x)
    visited = []
    print G.adj
    print stack
    while stack:
#        print ("stack %s" % (stack))
#        print ("visited %s" % (visited))
        tree = []
        if stack[-1] in visited:
            stack.pop()
            continue
        print("running DFS")
        reverseDFS(G,stack,visited,stack.pop(),tree)
        print("found tree %s" % (tree))
        

def main():
    [V,E,roads] = ipt()
    print roads
    G = Graph(V,E,roads)

    #finding intersections: Euler's Formula
    #"planar graph" is graph drawn in flat plane
    #without lines crossing (what we want)
    #Euler gives F - E + V = 2; or that
    #number of 'faces' (area in closed loop
    #of edges) minus num edges + num
    # vertices must be 2 for graph to be planar

main()
