#include<stdio.h>
#include<iostream>
#include<bitset>
using namespace std;
int numberOf1o(int n){
	int count = 0;
	unsigned int flag = 1;
	while(flag){
		if(flag&n){
			count++;		
		}
		flag=flag<<1;
	}
	return count;

}
int numberOf1t(int n){
	int count =0;
	int nsub=1;
	while(n){
		n = n&(n-1);
		count++;
	
	}
	return count;
}
void main(){
    int a=1223444;
	int b;
	cout<<bitset<sizeof(int)*8>(a)<<endl;
	b=numberOf1t(a);
	cout<<b;
	int c;
	cin>>c;


}