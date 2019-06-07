#include<stdio.h>

void left_rotate(unsigned long int arr[], unsigned long int n, unsigned long int d)
{
	unsigned long int a2[n], cnt=0;
	for(int i=0;i<d;i++)
	{
		for(unsigned long int i=1;i<n;i++)
		{
			a2[i-1] = arr[i];
		}
		a2[n-1] = arr[0];
		for(unsigned long int i=0;i<n;i++)
		{
			arr[i]=a2[i];
		}
	}
	for(unsigned long int i=0;i<n;i++)
	{
		printf("%lu ", a2[i]);
	}
}

int main()
{
	unsigned long int n,d,num,i;
	scanf("%lu %lu", &n,&d);
	unsigned long int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%lu", &num);
		a[i]=num;
	}
	left_rotate(a,n,d);
	return 0;
}
