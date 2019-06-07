#include<iostream>
using namespace std;

main()
{
	int i,T, P1, P2, K, sum, di;
	cin>>T;
	for(i=0;i<T;i++)
	{
		sum = 0;
		di = 0;
		cin>>P1>>P2>>K;
		sum = P1+P2;
		di = sum/K;
		if(di%2==0)
		{
			cout<<"CHEF"<<endl;
		}
		else
		{
			cout<<"COOK"<<endl;
		}
	}
}
	
