#include <iostream>
using namespace std;
int Min(int* arr,int length){
	//如果输入不正确
	//得到数组首位的指针
	if(arr==NULL||length<=0){
		return 0;
	}
	int* pStart = arr;
	int endIndex = length-1;
	int startIndex = 0;
	int tempIndex = 0;
	int count=5;


	//比较前后的数值并更新指针
	//条件为指针不能越界
	while(startIndex<endIndex){
		if(arr[startIndex]<arr[tempIndex]){
			startIndex = tempIndex;
			tempIndex = (endIndex+startIndex)/2;
			
		}else if(arr[startIndex]>arr[tempIndex]){
			endIndex = tempIndex;
			tempIndex = (endIndex+startIndex)/2;
		}else if (endIndex-startIndex ==1){
			tempIndex = endIndex;
			break;		
		}
	}
	return arr[tempIndex];
}
int main(){
	int arr[] = {5,6,7,1,2,3};
	cout<<"start"<<endl;
    int f = Min(arr,5);
	cout<<f;
	int st;
	cin>>st;
	return 0;
}