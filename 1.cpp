#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

void printVector(vector<int> V)
{
	for (int i = 0; i < V.size(); i++)
	{
		cout << V.at(i) << ",";
	}
	cout << endl;
}

//funciton populates vectors P and Q from the input file; also gets N
//void loadVectors(vector<int> &P, vector< vector<int> > &Q, int &N)
void loadVectors(vector<int> &P, vector<int> &Q, int &N)
{
	ifstream input;
	input.open("input.txt");

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

	vector<int> indices;
	vector<int> values;

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

void countIntersections(vector<int> &P, vector<int> &Q, int N, int &n_inter)
{
	if (N == 1)
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
	countIntersections(P, Q, N-1, n_inter);	
}

int main()
{

	int N;
	int n_inter = 0;
	vector<int> P;
	//vector< vector<int> > Q; 
	//Q values are tuples; order is [original index, value]
	//will be sorted based on value, need to preserve original index
	vector<int> Q;

	loadVectors(P, Q, N);

	printVector(P);
	printVector(Q);

	countIntersections(P, Q, N-1, n_inter);

	cout << "# inter = " << n_inter;

	return 0;
}
