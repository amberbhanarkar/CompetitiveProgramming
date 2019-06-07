#include<stdio.h>

void left_rotate(int arr[], int n, int d)
{
	int a2[n];
	for(int i=0;i<n;i++)
	{
		a2[i]=0;
	}
	printf("\n");
	for(int i=0;i<n;i++)
	{
		printf("%d", a2[i]);
	}
	for(int i=d;i<n;i++)
	{
		a2[i-d]=arr[i];
	}
	printf("\n");
	for(int i=0;i<n;i++)
	{
		printf("%d", a2[i]);
	}
	for(int i=0;i<d;i++)
	{
		a2[i+d]=arr[i];
	}
	printf("\n");
	for(int i=0;i<n;i++)
	{
		printf("%d", a2[i]);
	}
}

int main()
{
	int n,d,num,i;
	scanf("%d %d", &n,&d);
	int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d", &num);
		a[i]=num;
	}
	for(int i=0;i<n;i++)
	{
		printf("%d", a[i]);
	}
	left_rotate(a,n,d);
	return 0;
}
