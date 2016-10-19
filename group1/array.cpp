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








void merge(int* &A, int begin, int middle, int end)
{
	//merge sort heavily based on that of quiz.geeksforgeeks.org/merge-sort/
	cout << "merge with begin=" << begin << " middle=" << middle << " end=" << end << endl;

	int tmp1 = middle - begin + 1;
	int tmp2 = end - middle;

	int L[tmp1];
	int R[tmp2];

	for (int i = 0; i <= tmp1; i++)
		L[i] = A[begin+i];
	for (int i = 0; i <= tmp2; i++)
		R[i] = A[middle + begin + i];
	
	int i = 0;
	int j = 0;
	int k = begin;
	while(i < tmp1 && j < tmp2)
	{
		if (L[i] <= R[j])
		{
			A[k] = L[i];
			i++;
		}
		else
		{
			A[k] = R[j];
			j++;
		}
		k++;
	}

	while (i < tmp1)
	{
		A[k] = L[i];
		i++;
		k++;
	}

	while (j < tmp2)
	{
		A[k] = R[j];
		j++;
		k++;
	}
	for (int i = begin; i <= end; i++)
		cout << A[i] << ",";
	cout << endl;
}

void mergeSort(int* arry, int begin, int end)
{
	cout << endl;
	cout << "mergesort with begin=" << begin << " & end=" << end << " arry=";
	for (int i = begin; i < end; i++)
		cout << arry[i] << ",";
	cout << endl;
	
	if (begin < end)
	{
		int mid = begin+(end-1)/2;
		mergeSort(arry, begin, mid);
		mergeSort(arry, mid+1, end);

		merge(arry, begin, mid, end);
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

	int qarry[N];
	for (int i = 0; i < N; i++)
	{
		qarry[i] = Q.at(i);
		cout << qarry[i] << ",";
	}
	cout << endl;

	nsquared(P, Q, N-1, n_inter);

	tmp = n_inter;
	n_inter = 0;

	mergeSort(qarry, 0, N-1);

	for (int i = 0; i < N; i++)
		cout << qarry[i] << ",";
	cout << endl;

	cout << "Algorithm #1 found # inter = " << tmp << endl;

	cout << "Algorithm #2 found # inter = " << n_inter << endl;

	outputFile(n_inter, "output.txt");

	return 0;
}
