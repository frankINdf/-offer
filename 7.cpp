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
			//这里不使用引用可以么？？
			T data = stack1.top();
			stack1.pop();
			stack2.push(data);		
		}
	
	}
	if(stack2.size==0){
		throw new exception("empty");
	}
	T head = stack2.top();
	//换到s2后不用换回来，等s2出完再一次性把s1中弹入s2;
	stack2.pop();
	return head;

}
/*template <typename T> CQueue<T>::appendTail(const T& node){
	stack1.push(node);
}*/

/*
模板定义
template <typename T> class{}
类定义时别忘了构造函数是public
定义方法template name::方法名(){}
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
