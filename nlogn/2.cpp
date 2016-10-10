#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;



//function which prints a given vector 
void printVector(vector<int> V)
{
	for (int i = 0; i < V.size(); ++i)
	{
		cout << V.at(i) << ",";
	}
	cout << endl;
}



//function loads P, Q and N from input.txt file
//output: void
//input: integer vector P, Q and integer N (the total number)
void loadVectors(vector<int> &P, vector<int> &Q, int &N)
{
	ifstream input;					
	input.open("input.txt");

	char c_temp;
	char c_arry[5];
	int i = 0; //length of number

	while (input.get(c_temp))
	{
		if (c_temp == '\n')
			break; //leaves us on line 2
		c_arry[i] = c_temp;
		++i;
	}

	//convert string to int
	N = atoi(c_arry);	

	cout << "N=" << N << endl;		//display

	//set array back to nothing
	for (int j = 0; j < 5; ++j)
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
			for (int j = 0; j < 5; ++j)
				c_arry[j] = ' ';
			i = 0; //reset length of number
			input.get(c_temp); //skip commas
		}
		else if (c_temp == '\n')
		{
			//if there's nothing
			P.push_back(atoi(c_arry));
			break;
		}
		c_arry[i] = c_temp;
		++i;
	}	
			

	for (int j = 0; j < 5; ++j)
		c_arry[j] = ' ';
	i = 0; //reset length of # input
	int idx = 0;


	//get Qn
	while (input.get(c_temp))
	{
		if (c_temp == ',')
		{
			Q.push_back(atoi(c_arry));
			//reset c_arry
			for (int j = 0; j < 5; ++j)
				c_arry[j] = ' ';
			i = 0; //reset length of number
			input.get(c_temp);

		}
		else if (c_temp == '\n')
		{
		//if it's empty
			Q.push_back(atoi(c_arry));
			break;
		}
		c_arry[i] = c_temp;
		++i;
	}


	input.close();		//close input buffer
}




void countIntersectionsRec(vector<int> &P, vector<int> &Q, int N, int &n_inter)
{
	if (N == 0)
		return;
	cout << endl; cout << endl;
	cout << "N=" << N << endl;
	//algorithm: for Pn, count pairs of Qi,Pi for which Qi > Qn but Pi < Pn
	for (int i = 0; i < N; ++i) //check Pi for i < N
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
	countIntersectionsRec(P, Q, N-1, n_inter);	
}

//currently doesn't work fully, only catches some
void countIntersections(vector<int> &P, vector<int> &Q, int N, int &n_inter)
{
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			if (Q.at(j) > Q.at(i))
			{
				cout << "Q" << i << "= " << Q.at(j) << " & Qn = " << Q.at(i) << endl;
				if (P.at(j) < P.at(i))
				{
					cout << "P" << i << "= " << P.at(j) << " & Qn = " << P.at(i) << endl;
					n_inter++;
				}
			}
		}
	}
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

	countIntersectionsRec(P, Q, N-1, n_inter);

	cout << "rec # inter = " << n_inter << endl;

	n_inter = 0;

	countIntersections(P, Q, N-1, n_inter);
	
	cout << "inter = " << n_inter << endl;

	return 0;
}
