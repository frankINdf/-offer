#include <stdio.h>
#include<iostream>  
#include <stack>
using namespace std;
typedef struct ListNode
{
	int m_nkey;
	struct ListNode* next;
} NODE;
void PrintListReversingly(NODE *phead){
	std::stack<NODE*> nodes;
	NODE* pNode = phead;
	
	while(pNode != NULL){
		nodes.push(pNode);
		pNode = pNode->next;

	}
	while(!nodes.empty()){
	    pNode = nodes.top();
		cout<<"out"<<pNode->m_nkey<<"\n";
		nodes.pop();
	}
	cout<<endl;

}
int main(){
	int a=0;

	NODE* head = new NODE;
	NODE* l1= new NODE;
	NODE* l2= new NODE;

	head->next=l1;
	head->m_nkey=6;
	l1->m_nkey = 2;
	l1->next = l2;
	l2->m_nkey=5;
	l2->next = NULL;
	PrintListReversingly(head);
	int c;
	cin>>c;



	return 0;
}