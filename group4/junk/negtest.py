import random;
import sys;
import os;
import re;

class Graph:
    def __init__(self,V,vertices):
        self.adj = dict(zip(vertices,[[] for x in vertices]))
        
    def add_edge(self,to,fr):
        self.adj[fr].append(to)

    adj = dict()

def ipt():
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    #get roads as vertex pairs
    #roads are of form 'first vertex,second vertex'
    #negation of a road is signalled by negative sign pf first vertex
    for i in range(0,int(E)):
        roads[i] = roads[i] +','+ roads[i+1] 
        roads.pop(i+1)
    vertices = []
    for x in roads:
        vertices.append(x)
        vertices.append('-'+x)
    return [int(V),int(E),vertices]

def main():
    [V,E,vertices] = ipt()
    G = Graph(V,vertices)
    print G.adj
    


main()
