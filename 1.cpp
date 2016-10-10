#include <iostream>
#include <fstream>
#include <deque>
#include <cstdlib>
#include <algorithm>

using namespace std;

void printVector(deque<int> V)
{
	for (int i = 0; i < V.size(); i++)
	{
		cout << V.at(i) << ",";
	}
	cout << endl;
}

//funciton populates deques P and Q from the input file; also gets N
//void loadVectors(deque<int> &P, vector< vector<int> > &Q, int &N)
void loadVectors(deque<int> &P, deque<int> &Q, int &N, char* filename)
{
	ifstream input;
	input.open(filename);

	//use this space to get stuff
	char c_temp;
	char c_arry[5];
	int i = 0; //length of number
	//super awkward way but whatever it works
	while (input.get(c_temp))
	{
		if (c_temp == '\n')
			break; //leaves us on line 2
		c_arry[i] = c_temp;
		i++;
	}
	N = atoi(c_arry);	
	cout << "N=" << N << endl;

	for (int j = 0; j < 5; j++)
		c_arry[j] = ' ';

	i = 0; //reset length of # input
	//line 2 is the values of Pn
	while (input.get(c_temp)) //get pn
	{
		//sloppy case tree; if we lose numbers look here for problems first
		if (c_temp == ',')
		{
			P.push_back(atoi(c_arry));
			//reset c_arry
			for (int j = 0; j < 5; j++)
				c_arry[j] = ' ';
			i = 0; //reset length of number
			input.get(c_temp); //skip commas
		}
		else if (c_temp == '\n')
		{
			//does this work if line is empty?
			P.push_back(atoi(c_arry));
			break;
		}
		c_arry[i] = c_temp;
		i++;
	}	
			

	for (int j = 0; j < 5; j++)
		c_arry[j] = ' ';
	i = 0; //reset length of # input
	int idx = 0;

	while (input.get(c_temp))
	{
		if (c_temp == ',')
		{
			Q.push_back(atoi(c_arry));
			//reset c_arry
			for (int j = 0; j < 5; j++)
				c_arry[j] = ' ';
			i = 0; //reset length of number
			input.get(c_temp);

		}
		else if (c_temp == '\n')
		{
			Q.push_back(atoi(c_arry));
			break;
		}
		c_arry[i] = c_temp;
		i++;
	}


	//scrapped idea, disregard
	/*

	deque<int> indices;
	deque<int> values;

	//loop needs to fill Q by giving original index values
	//and appropriately reading from input.txt

	while (input.get(c_temp))
	{
		if (c_temp == '\n')
		{
			indices.push_back(idx);
			values.push_back(atoi(c_arry));
			idx++; //index is collected
			break;
		}
		if (c_temp == ',')
		{
			values.push_back(atoi(c_arry));
			for (int j = 0; j < 5; j++)
				c_arry[j] = ' ';
			i = 0; //reset length of number
			input.get(c_temp);
			indices.push_back(idx);
			idx++; //index is collected
		}
		c_arry[i] = c_temp;
		i++;
	}

	Q.push_back(indices);
	Q.push_back(values);

	printVector(Q.front());
	printVector(Q.back());
	*/


	input.close();
}

void nsquared(deque<int> &P, deque<int> &Q, int N, int &n_inter)
{
	if (N == 0)
		return;
	cout << endl; cout << endl;
	cout << "N=" << N << endl;
	//algorithm: for Pn, count pairs of Qi,Pi for which Qi > Qn but Pi < Pn
	for (int i = 0; i < N; i++) //check Pi for i < N
	{
		cout << "Q" << i << "= " << Q.at(i) << " & Qn = " << Q.at(N) << endl;
		if (Q.at(i) > Q.at(N))
		{
			cout << "check p" << endl;
			cout << "P" << i << "= " << P.at(i) << " & Qn = " << P.at(N) << endl;
			if (P.at(i) < P.at(N))
			{
				cout << "INTERSECTION" << endl;
				n_inter++;
			}
		}
	}
	nsquared(P, Q, N-1, n_inter);	
}

//in order to get nlogn complexity, need the recursion tree to double in # nodes each time
//(call itself twice, each with half the size). How to do this? Maybe we can eliminate
//a set of points if they can't intersect to work with a smaller data set?

//What about a set of points can we divide in half? Probably by their magnitudes, i.e. divide
//a set into the larger and smaller half. But how would we be able to count intersections that
//occured between a larger and smaller point...

//maybe the best solution is to, for each point, do a log(n) operation; that way since we run that
//operation n times our algorithm will be nlog(n) right?

//log(n) operations are similar to binary search; maybe we could run a binary search for each of the
//n points to find intersections that way? Doesn't sound unworkable.

//I think a key crossover from the n^2 algorithm above is reducing the size of the problem each time
//a Pn value is examined. Maybe we can approach finding intersections the same way...

//disregard above spitballing lol. Implementing algorithm from the source we found




void merge(deque<int> &Q, int begin, int middle, int end, int &n_inter)
{
	//cognitive dissonance warning: Q is not always the entire array of Q
	//but is labled so to make below comparisons between Qi and Qj more intuitive

	//drew on https://courses.engr.illinois.edu/cs374/homework/hw4.pdf
	
	//compute # index pairs i<j for which Qi > Qj [this results in an intersection]
	//mergesort is nlogn time, so use a modified version of it	
	deque<int> V;
	int i = begin;
	int j = middle+1;
	cout << endl << "Running merge with begin=" << begin << " middle=" << middle << " end=" << end << " Q=";
	printVector(Q);
	
	for (int k = begin; k <= end; k++)
	{
		cout << "k=" << k << " ";
		cout << "i=" << i << " j=" << j << " Qi=" << Q.at(i) << " Qj=" << Q.at(j);
		cout << endl;
	}
	cout << endl;
	

	/*for (int k = begin; k <= end; k++)
	{
		//need to find: when i < j, Qi > Qj
		cout << "i=" << i << " j=" << j << " Qi=" << Q.at(i) << " Qj=" << Q.at(j);
		if (j >= end)
		{
			if (Q.at(i) > Q.at(j))
			{
				cout << " INTER";
				n_inter++;
				cout << "Va pushing front " << Q.at(j);
				V.push_front(Q.at(j));
			}
			else 
			{
				cout << "Va pushing front " << Q.at(i);
				V.push_front(Q.at(i));
			}
			i++;
		}
		else if (i >= middle)
		{
			if (Q.at(i) > Q.at(j))
			{
				cout << " INTER";
				n_inter++;
				cout << "Vb pushing front " << Q.at(j);
				V.push_front(Q.at(j));
			}
			else
			{	
				V.push_front(Q.at(i));
				cout << "Vb pushing front " << Q.at(i);
			}
			j++;
		}
		else if (Q.at(i) > Q.at(j)) //INTERSECTiON
		{
			cout << " INTER";
			n_inter++;
			cout << "Vc pushing front " << Q.at(j);
			V.push_front(Q.at(j));
			j++;
		}
		else if (Q.at(i) < Q.at(j))
		{
			cout << "Vd pushing front " << Q.at(i);
			V.push_front(Q.at(i));
			if (i+1 == j)
			{
				j++;
				i++;
			}
			else i++;
		}

		cout << endl;
	}*/
	cout << "V=";
	printVector(V);
	//loop to copy work into real array if really sorting
}

void mergeSort(deque<int> &Q, int begin, int end, int &n_inter)
{
	cout << '\t' << "mergeSort with begin=" << begin << " end=" << end << " Q=";
	printVector(Q);
	if ((end - begin) <= 1) //if size of array is 1, don't do anything
		return; //base case
	printVector(Q);
	int middle = (end+begin)/2;
	mergeSort(Q, begin, middle, n_inter);
	mergeSort(Q, middle, end, n_inter);
	merge(Q, begin, middle, end, n_inter);
}

void outputFile(int n_inter, char* filename)
{
	fstream output;
	output.open(filename);
	output << n_inter;
	output.close();
	cout << "outputting to file " << filename << " the number " << n_inter << endl;
}


int main(int argc, char* argv[])
{

	int N;
	int n_inter = 0;
	int tmp;
	deque<int> P;
	//deque< vector<int> > Q; 
	//Q values are tuples; order is [original index, value]
	//will be sorted based on value, need to preserve original index
	deque<int> Q;


	loadVectors(P, Q, N, argv[1]);

	printVector(P);
	printVector(Q);

	nsquared(P, Q, N-1, n_inter);

	tmp = n_inter;
	n_inter = 0;

	mergeSort(Q, 0, Q.size()-1, n_inter);

	cout << "Algorithm #1 found # inter = " << tmp << endl;

	cout << "Algorithm #2 found # inter = " << n_inter << endl;

	//sorta sloppy but gets the job one; outputs to file output.txt as required
	outputFile(n_inter, "output.txt");

	return 0;
}
