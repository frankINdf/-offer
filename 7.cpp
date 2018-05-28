#include <stack>
using namespace std;
#include<exception> 
#include <iostream>
template <typename T>class CQueue{
public:
	CQueue(void);
	~CQueue(void);
	void appendTail(const T& node);
	T deleteHead();
private:
	stack<T> stack1;
	stack<T> stack2;
};
template<typename T> CQueue<T>::CQueue(void){
}
template<typename T> CQueue<T>::~CQueue(void){
}
template<typename T> void CQueue<T>::appendTail(const T& node){
	stack1.push(node);
}
template<typename T> T CQueue<T>::deleteHead(){
	if(stack2.size()<=0){
		while(stack1.size()>0){
			//���ﲻʹ�����ÿ���ô����
			T data = stack1.top();
			stack1.pop();
			stack2.push(data);		
		}
	
	}
	if(stack2.size==0){
		throw new exception("empty");
	}
	T head = stack2.top();
	//����s2���û���������s2������һ���԰�s1�е���s2;
	stack2.pop();
	return head;

}
/*template <typename T> CQueue<T>::appendTail(const T& node){
	stack1.push(node);
}*/

/*
ģ�嶨��
template <typename T> class{}
�ඨ��ʱ�����˹��캯����public
���巽��template name::������(){}
*/
void main(){
    CQueue<int> queue; 
	int a=1,b=2,c=3,d=4;
	queue.appendTail(a);  
    queue.appendTail(b);  
    queue.appendTail(c);  
    int head;
	head=queue.deleteHead();
	cout<<head<<endl;
	head=queue.deleteHead();  
    cout<<head<<endl;  
    queue.appendTail(d);  
    head=queue.deleteHead();  
    cout<<head<<endl;  
    head=queue.deleteHead();  
    cout<<head<<endl; 
    cout<<head<<endl;  

	int f;
	cin>>f;


}
