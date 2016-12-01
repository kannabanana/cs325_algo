import random;
import os;
import sys;
import re;

def tru(x):
    tup = (x[0],x[1],True)
    return tup

def neg(x):
    tup = (x[0],x[1],False)
    return tup

def flip(x):
    tup = [0,0,0]
    ret = (0,0,0)
    if x[2] == False:
        tup[0] = x[0]
        tup[1] = x[1]
        tup[2] = True
        ret = tuple(tup)
    else:
        tup[0] = x[0]
        tup[1] = x[1]
        tup[2] = False
        ret = tuple(tup)
    return ret
        

class Graph:
    def __init__(self,V,edges):
        #takes in # vertices, list of all edges
        self.V = V
        #adjacency list for graph
        self.vertices = []
        added = []
        for x in edges:
            pair = x
            print pair
            if pair[0] not in added:
                self.vertices.append(tru(pair[0]))
                self.vertices.append(neg(pair[0]))
                added.append(pair[0])
            if pair[1] not in added:
                self.vertices.append(tru(pair[1]))
                self.vertices.append(neg(pair[1]))
                added.append(pair[1])
        self.adj = dict(zip(self.vertices,[[] for i in range(0,4*V)]))
        self.rev = dict(zip(self.vertices,[[] for i in range(0,4*V)]))
        for x in edges:
            #add x[0] OR x[1]
            self.adj[neg(x[0])].append(tru(x[1]))
            self.adj[neg(x[1])].append(tru(x[0]))
            self.rev[tru(x[0])].append(neg(x[1]))
            self.rev[tru(x[1])].append(neg(x[0]))


            #add !x[0] OR !x[1]
            self.adj[tru(x[0])].append(neg(x[1]))
            self.adj[tru(x[1])].append(neg(x[0]))
            self.rev[neg(x[0])].append(tru(x[1]))
            self.rev[neg(x[1])].append(tru(x[0]))

    V = 0
    adj = dict()
    rev = dict()
    vertices = []

def ipt():
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    edges = []
    for i in range(0,int(E)):
        edges.append((int(roads[i]),int(roads[i+1])))
        roads.pop(i+1)
    return [int(V),edges]

def YES():
    fo = open("output.txt",'w')
    fo.write("YES")
    fo.close()

def NO():
    fo = open("output.txt",'w')
    fo.write("NO")
    fo.close()

def find_crossings(edges):
    inters = []
    for x in range(0,len(edges)):
#        print "looking at"
#        print edges[x]
        for y in range(0,x):
#            print "compare with"
#            print edges[y]
            if edges[y][0] > edges[x][0] and edges[y][1] > edges[x][1]:
                print("%s > %s and %s > %s" % (edges[y][0], edges[x][0], edges[y][1], edges[x][1]))
                inters.append((edges[x],edges[y]))
            #if edges[y][0] < edges[x][0] and edges[y][1] < edges[x][1]:
            #    print("%s < %s and %s < %s" % (edges[y][0], edges[x][0], edges[y][1], edges[x][1]))
            #    inters.append((edges[x],edges[y]))

    return inters

def initialDFS(G,stack,visited,curr):
 #   print curr
    if curr in visited:
        return
    visited.append(curr)
    for x in G.adj[curr]:
        initialDFS(G,stack,visited,x)
    stack.append(curr)

def reverseDFS(G,stack,visited,curr,tree):
    if curr in visited:
        return
    visited.append(curr)
    tree.append(curr)
    for t in G.rev[curr]:
        reverseDFS(G,stack,visited,t,tree)

#TODO: correctly check if a 2-way path exists between item & its negation
#maybe correct kosaraju?

def Kosaraju(inters):
    G = Graph(len(inters),inters)
    print G.adj

    #GOT EM IN 2CNF FORM BABY

    visited = []
    stack = []
    for x in G.vertices: #number of edges/OR pairs in 2cnf form
        initialDFS(G,stack,visited,x)
   # print stack
    visited = []
    forest = []
    while stack:
        tree = []
        if stack[-1] in visited:
            stack.pop()
            continue
        reverseDFS(G,stack,visited,stack.pop(),tree)
        forest.append(tree)
    print "forest"
    print forest
    return True

def main():
    [V,edges] = ipt()
    inters = find_crossings(edges)
    #2CNF formula for paths that intersect
    print inters
    if not inters:
        YES()
        #obviously no problems if lines never intersect
    if Kosaraju(inters) == True:
        YES()
   # else:
   #     NO()




main()
