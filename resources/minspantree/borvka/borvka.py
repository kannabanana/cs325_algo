def getKey(item):
	return item[0]


#check that the vertex is not in A
def check(A,w,x):
	l = len(A)
	i = 0
	for x in range(0,l):
		if(i ==0):
		
			
		else:
			break

	return i	


def main():
	A = ()
	A = list(A)
	temp = ()
	temp = list(temp)
	lst = (('a', 'b', 7),('a', 'c', 9),('a', 'f', 14),('b', 'c', 10),('b', 'd', 15),('c', 'd', 11),('c', 'f', 2),('d', 'e', 6),('e', 'f', 9))
	w = sorted(lst,key=getKey)
	print w
	l = len(lst)

	for x in range (0,l):
		print w[x][2]
		i = check(A,w,x)
		if(i != 1):
			temp.append(w[x][0])
			temp.append(w[x][1])
			A.append(temp)
		
			temp = ()
			temp = list(temp)

	#while I haven't checked all the nodes yet
		#check if they belong to the same dijoined set
			#if they don't, push them to the tuple A
		#if they do, move on to the next one

	print A
main()
