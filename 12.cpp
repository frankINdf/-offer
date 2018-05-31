#include <iostream>
using namespace std;
void printNumber(char* a);
void printNumberi(char* a);
//构造函数深度优先遍历
void Print1ToMaxOfDigits(char* number,int length, int index){
	if(index == length)
	{
		printNumber(number);
		return;
	}
	for(int i=0;i<10;i++){
		//cout<<index;
		number[index] = i+'0';
		Print1ToMaxOfDigits(number,length,index+1);
	}


}
//
void print1ToMaxNumber(int n){
	if(n == 0){
		return;	
	}
	char* number = new char[n+1];
	number[n]='\0';

    Print1ToMaxOfDigits(number,n,0);
}
//
void printNumber(char* a){
	int i=0;
	while(*(a+i)=='0'){
		i++;	
	}
	if(i==strlen(a))
		cout<<0<<endl;
	if(i!=strlen(a))
	    cout<<(a+i)<<endl;
}
void main(){
	char *a = new char[3];

	a[0]='0';
	a[1]='0';
	a[2]='\0';
	print1ToMaxNumber(3);
	int stop;
	cin>>stop;


}
	
