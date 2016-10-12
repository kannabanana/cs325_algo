#include <iostream>
#include <fstream>
#include <deque>
#include <cstdlib>
#include <algorithm>

using namespace std;

void printDeque(deque<int> V)
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
//	cout << "N=" << N << endl;

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

	input.close();
}

void nsquared(deque<int> &P, deque<int> &Q, int N, int &n_inter)
{
	if (N == 0)
		return;
//	cout << endl; cout << endl;
//	cout << "N=" << N << endl;
	//algorithm: for Pn, count pairs of Qi,Pi for which Qi > Qn but Pi < Pn
	for (int i = 0; i < N; i++) //check Pi for i < N
	{
//		cout << "Q" << i << "= " << Q.at(i) << " & Qn = " << Q.at(N) << endl;
		if (Q.at(i) > Q.at(N))
		{
//			cout << "check p" << endl;
//			cout << "P" << i << "= " << P.at(i) << " & Qn = " << P.at(N) << endl;
			if (P.at(i) < P.at(N))
			{
//				cout << "INTERSECTION" << endl;
				n_inter++;
			}
		}
	}
	nsquared(P, Q, N-1, n_inter);	
}

void outputFile(int n_inter, char* filename)
{
	fstream output;
	output.open(filename);
	output << n_inter;
	output.close();
//	cout << "outputting to file " << filename << " the number " << n_inter << endl;
}








deque<int> merge(deque<int> A, int begin, int middle, int end)
{

	cout << "merge with begin=" << begin << " middle=" << middle << " end=" << end << endl;

	deque<int> L; //work arrays
	deque<int> R;

	deque<int> ret;
	if (begin+1 == end)
	{
		L.push_back(A.at(begin));
		R.push_back(A.at(end));
	}
	else
	{
		for (int i = begin; i <= middle; i++)
			L.push_back(A.at(i));
		for (int i = middle+1; i <= end; i++)
			R.push_back(A.at(i));
	}
	cout << "L=";
	printDeque(L);
	cout << "R=";
	printDeque(R);
	
	int i = begin;
	int j = middle;
	while(i < middle && j < end)
	{
		if (L.at(i) <= R.at(j))
		{
			ret.push_back(L.at(i));
			i++;
		}
		else
		{
			ret.push_back(R.at(j));
			j++;
		}
	}

	while (i = middle)
	{
		ret.push_back(L.at(i));
		i++;
	}

	while (j < end)
	{
		ret.push_back(R.at(j));
		j++;
	}
	cout << "ret=";
	printDeque(ret);
	return ret;
}

void mergeSort(deque<int> &Q, int begin, int end)
{
	cout << endl;
	cout << "mergesort with begin=" << begin << " & end=" << end << " arry=";
	printDeque(Q);
	if (begin < end)
	{
		int mid = (end+begin)/2;
		/*deque<int> LO;
		for (int i = begin; i <= mid; i++)
			LO.push_back(Q.at(i));
		cout << "LO=";
		printDeque(LO);
		deque<int> HI;
		for (int i = mid+1; i <= end; i++)
			HI.push_back(Q.at(i));
		cout << "HI=";
		printDeque(HI);*/
		mergeSort(Q, begin, mid);
		mergeSort(Q, mid+1, end);

		Q = merge(Q, begin, mid, end);
	}
}

int main(int argc, char* argv[])
{

	int N;
	int n_inter = 0;
	int tmp;
	deque<int> P;
	deque<int> Q;


	loadVectors(P, Q, N, argv[1]);
	
	nsquared(P, Q, N-1, n_inter);

	tmp = n_inter;
	n_inter = 0;

	mergeSort(Q, 0, Q.size()-1);

	printDeque(Q);

	cout << "Algorithm #1 found # inter = " << tmp << endl;

	cout << "Algorithm #2 found # inter = " << n_inter << endl;

	outputFile(n_inter, "output.txt");

	return 0;
}
