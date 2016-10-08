#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

//funciton populates vectors P and Q from the input file; also gets N
void loadVectors(vector<int>* P, vector<int>* Q, int* N)
{
	ifstream input;
	input.open("input.txt");

	//use this space to get stuff
	char c_temp;
	int n_temp = 0;
	int i = 0;
	while (input.get(c_temp))
	{
		if (c_temp == '\n')
			break;
		cout << c_temp << endl;
		cout << atoi(c_temp) << endl;
		n_temp++;
	}
	input.close();
}

int main()
{

	int N;
	vector<int> P;
	vector<int> Q;

	loadVectors(&P, &Q, &N);

	
	return 0;
}
