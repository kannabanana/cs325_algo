import random;
import sys;
import os;
import re;

class Graph:
    #constructor
    def __init__(self,V,edges,roads):
        self.vertexRange = [i for i in range(1,V+1)]
        self.vertexRange.extend([i for i in range(-V,0)]) 
        self.adj = dict(zip(self.vertexRange,[[] for x in range(0,2*V)]))
        self.rev = dict(zip(self.vertexRange,[[] for x in range(0,2*V)]))
        self.roadmap = dict(zip(range(1,1+len(roads)),roads))
        
    def add_edge(self,fr,to):
#        print("link from %s to %s" % (fr, to))
        self.adj[fr].append(to)
        self.rev[to].append(fr)

    #adjacency list for directed graph
    adj = dict()
    rev = dict()
    #roadmap maps index numbers to respective roads
    roadmap = dict()
    vertexRange = []

def ipt(): #gets input from file, indexes the roads
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    for i in range(0,int(E)):
        #replace with tuples if things get tricky with access
        roads[i] = '('+roads[i] +','+ roads[i+1]+')'
        roads.pop(i+1)
    edges = []
    #roads are numbered; 'negations' of roads are negative #s
    for x in range(1,1+len(roads)):
        edges.append(x)
        edges.append(-x)
        #HUGE TRADEOFF, BE CAREFUL: indexing for vertices is OFF BY ONE
    return [int(V),int(E),roads,edges]

def populate_edges(G,edges,roads):
#    print roads
    for x in roads:
        ints = x[:-1][1:].split(',')
        pair = (int(ints[0])+1,int(ints[1])+1)
        #actually turn it into tuple for ease of use
        G.add_edge(-pair[0],-pair[1])
        G.add_edge(pair[0],pair[1])
        G.add_edge(-pair[1],-pair[0])
        G.add_edge(pair[1],pair[0])

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
    #V is # if vertexes (houses)
    #E is # edges (roads)
    #roads = list of house pairs that roads are between
    #vertices = indexed roads, represented inside and outside circle
    [V,E,roads,edges] = ipt()
    #CAREFUL graph is not describing the ring road but is part of 2SAT
    G = Graph(V,edges,roads)
#    print G.roadmap
#    print G.adj

    populate_edges(G,edges,roads)

    #run Kosaraju's algorithm to find strongly connected components
    Kosaraju(G)
    print G.adj
    


main()
