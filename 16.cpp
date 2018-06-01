#include <iostream>
using namespace std;
struct ListNode
{
	int value;
	ListNode* next;
};
ListNode* reverseNode(ListNode* head)
{
	//Node为NULL
	ListNode* pNode = NULL;
	if(head == NULL){
		return NULL;
	}
	else if(!head->next)
	{

		return head;
	}else{

		pNode = head;
		ListNode* pNext = pNode;
		ListNode* pPre = NULL;
		while(pNode->next!=NULL){
		//	cout<<pNode->value;
			pNext = pNode->next;
			pNode->next = pPre;
			pPre = pNode;
			pNode = pNext;		
		}
		return pNode;
	}
	
	//只有一个Node，返回该Node

	
}
void main(){
	ListNode* a = new ListNode();
	ListNode* b = new ListNode();
	ListNode* c = new ListNode();
	ListNode* d = new ListNode();
	ListNode* e = new ListNode();
	a->next = b;
	b->next = c;
	c->next = d;
	d->next = e;
	d->next = NULL;
	a->value =1;
	b->value =2;
	c->value =3;
	d->value =4;
	ListNode* h= new ListNode();
	h=NULL;
    ListNode* f = new ListNode();
    f->value =10;
	//f->next=NULL;
    //ListNode* ph = reverseNode(f);
	cout<<(!f->next);
	int stop;
	cin>>stop;
}