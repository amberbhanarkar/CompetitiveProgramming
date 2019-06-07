#include<iostream>
using namespace std;

int main()
{
	int t, d,i;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>d;
		int x;
		x = d%9;
		cout << x + 1 << endl;
	}
	return(0);
}
