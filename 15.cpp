#include<iostream>
using namespace std;
struct ListNode{
	int value;
	ListNode* next;
};
ListNode* findKthToTial(ListNode* head,int k)
{   //headÎªNULL»òk=0
	if(head==NULL||k==0){
		return NULL;	
	}
	int length = 0;
    //k>length
	ListNode* pNode=head;
	ListNode* pBack=NULL;
	int count = 0;
	while(count<k-1){
		pNode = pNode->next;
		count++;
		
	}
	
	pBack=head;
	while(pNode->next!=NULL){
		pNode = pNode->next;
        pBack=pBack->next;
	}
	return pBack;
	
}
void main()
{
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

    ListNode* k ;
	k= findKthToTial(a,3);
	cout<<k->value;
    unsigned int stop=0;
	cin>>stop;

}