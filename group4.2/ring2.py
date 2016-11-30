import random
import os
import string



#gets input from files
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



#function checks if there are crosses
#def check_cross(house):





def main():
	[V,E,roads,edges] = ipt()
 	print [V,E,roads]


main()
