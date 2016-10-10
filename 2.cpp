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
		++i;
	}
	N = atoi(c_arry);	
	cout << "N=" << N << endl;

	for (int j = 0; j < 5; ++j)
		c_arry[j] = ' ';

	i = 0; //reset length of # input
	//line 2 is the values of Pn
	while (input.get(c_temp)) //get pn
