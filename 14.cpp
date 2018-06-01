#include <iostream>
using namespace std;
bool isEven(int number){
	return (number&1)==0;
}

void partition(int* pstart,int length,bool (*func)(int))
{
	//定义两个指针
	int* pahead = pstart;
	int* pback = pstart+length-1;
	int* pNow = pstart;
	while(pahead<pback){
	    while(isEven(*pahead)){
		    pahead++;			
		}
	    while(!isEven(*pback)){
	        pback--;
		}
		if(pahead<pback)
		{
		    int temp = *pahead;
			*pahead = *pback;
			*pback = temp;
		}
	}
}
void main()
{
	int a[]={1,5,2,4,7,8};
	int length = 6;
	partition(a,length,isEven);
	cout<<a[0]<<a[1]<<a[2]<<a[3];
	int stop;
	cin>>stop;


}