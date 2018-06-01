#include<iostream>
using namespace std;
struct ListNode{
	int value;
	ListNode* next;
};
void deleteNode(ListNode* head,ListNode* node){
	//若没有元素

	//若删除尾部
	if(node->next==NULL){
	    ListNode* pNode=head;
		while(pNode->next!=node){
			pNode=pNode->next;		
		}
		pNode->next = NULL;
		delete node;
	}
	else if(head == node){
		head->next = NULL;
		delete node;
	}
	else{

	    //有多个元素
	    node->value = node->next->value;
		node->next = node->next->next;
	}
}

int main(){
	ListNode* a =  new ListNode;
	a->value=3;
	ListNode* b =  new ListNode;
	ListNode* c =  new ListNode;
	b->value=4;
	c->value=5;
	a->next = b;
	b->next = c;
	c->next = NULL;
	deleteNode(a,b);
	cout<<a->next->value;
	int stop;
	cin>>stop;
	return 1;
}