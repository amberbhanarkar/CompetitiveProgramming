#include <bits/stdc++.h>
using namespace std; 

unsigned int countSetBits(unsigned int n) 
{ 
	unsigned int count = 0; 
	while (n) { 
		count += n & 1; 
		n >>= 1; 
	} 
	return count; 
} 
void fastscan(int &number) 
{ 
    bool negative = false; 
    register int c; 
    number = 0; 
    c = getchar(); 
    if (c=='-') 
    { 
        negative = true; 
        c = getchar(); 
    } 
    for (; (c>47 && c<58); c=getchar()) 
        number = number *10 + c - 48; 
    if (negative) 
        number *= -1; 
} 
 
int main() 
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int T, i, N, Q, cnt; 
	fastscan(T);
	for(i=0;i<T;i++){
		fastscan(N);
		fastscan(Q);
		int a[N],aa,j,k, even=0,odd=0;
		for(j=0;j<N;j++){
			fastscan(aa);
			a[j]=aa;
			cnt = countSetBits(aa);
			if(cnt%2==0){
				even++;
			}
			else{
				odd++;
			}
		}
		for(j=0;j<Q;j++){
			int P, res1;
			fastscan(P);
			res1 = countSetBits(P);
			if(res1%2==0){
				cout<<even<<" "<<odd<<"\n";
			}
			else{
				cout<<odd<<" "<<even<<"\n";
			}
		}
	}
	return 0;
} 
