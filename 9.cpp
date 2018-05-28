#include <stdio.h>
#include <iostream>
using namespace std;
long
Fibonacci(unsigned n){
	int result[]={0,1};
	if(n<2){
		return result[n];	
	}
	while(n>=2){
		long temp = result[0]+result[1];
		result[n%2]=temp; 
		n--;
	}
	return result[n%2];


}
void main(){
	cout<<"8th"<<endl;
	int fb=Fibonacci(30);
	cout<<fb;
	int t;
	cin>>t;
}