import os
import string
import random

#SR Kanna
#Scheduling algorithm from scratch
#Algorithm:



#random function
#INPUT: LIST
def randomarray(schedule,l):

	aclass = [0,0]
	for x in range(0,l):
		x = random.randrange(100)
		y = random.randrange(100)	
		while y < x:
			y = random.randrange(100)
		aclass[0] = x
		aclass[1] = y
		schedule[x] = aclass

	return schedule

#scheduling function
#def jobscheduling(schedule):
	#base case - nothing
#	if not in schedule:
#		return
	#basecase - nothing is after it
	#what finishes first?
		#sort based on second index
			#print out the array index
			#recurse on all segments that end after the end time
				#sort and create another array based on what starts after


def main():
#	l = 10
#	schedule = []
#	schedule = randomarray(schedule,l);
#	print "final output is ",schedule

	schedule = [[0,4],[1,4],[1,3],[5,10],[4,7],[7,10],[6,9],[9,10],[3,7],[4,8]]
	print schedule
	schedule.sort()
	print schedule
main()
