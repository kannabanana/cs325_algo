#2CNF solver needed

#problem in 2CNF roads:  
#{(0,3)in OR (0,3)out} AND
#{(1,3)in OR (1,3)out} AND
#{(0,2)in OR (0,2)out} AND
#{(2,5)in OR (2,5)out} AND
#{(4,5)in OR (4,5)out} 

#idea: negation of path is outdside circle,
# non-negated literal is inside circle

import sys; 
import os;
import random; 
import re;

class Graph:
    def __init__(self,numVertices,labels):
        lit = [i for i in labels]
        neg = ['!' + i for i in labels]
        both = []
        for i in range(0,len(lit)):
            both.append(lit[i])
            both.append(neg[i])
        adj = dict(zip(both,[[] for x in both]))
        print adj

    def add_edge(self,fr,to):
        self.adj[fr].append(to)
        

    vertices = [] 
    #adjacency list 
    adj = dict()

def ipt():
    fo = open("input.txt",'r')
    [V,E] = fo.readline().rstrip().split(',')
    roads = fo.readline().split(',')
    #get roads as vertex pairs
    #roads will be list of form ['to,from', 'to,from',...]
    for i in range(0,int(E)):
        roads[i] = roads[i] + ';' +  roads[i+1]
        roads.pop(i+1)
    return [int(V),int(E),roads]

def yes():
    fo = open("output.txt",'w')
    fo.write("YES")
    fo.close()

def no():
    fo = open("output.txt",'w')
    fo.write("NO")
    fo.close()

def main():
    [V,E,roads] = ipt()
    print V
    print E
    print roads    

    G = Graph(len(roads),roads)
    print(G.adj['0;2'])


main()
