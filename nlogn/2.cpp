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





int main()
{

	int N;
	int n_inter = 0;	//number of intersections
	vector<int> P;
	vector<int> Q;

	//vector< vector<int> > Q; 
	//Q values are tuples; order is [original index, value]
	//will be sorted based on value, need to preserve original index

	loadVectors(P, Q, argv[1]);

	//printing the vectors loaded from input.txt
	printVector(P);
	printVector(Q);

	//countIntersectionsRec(P, Q, N-1, n_inter);
	//nlogn function call
	

	cout << "Nlogn Algorithm found # inter = " << n_inter << endl;

	outputFile(n_inter,"output.txt");

	return 0;
}
