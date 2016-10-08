#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

//funciton populates vectors P and Q from the input file; also gets N
void loadVectors(vector<int>* P, vector<int>* Q, int* N)
{
	ifstream input;
	input.open("input.txt");

	//use this space to get stuff

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
