#include <iostream>
using namespace std;
typedef struct TreeNode{
	int value;
	TreeNode* rightNode;
	TreeNode* leftNode;

} Node;


Node* ConstructCore(int* startPreorder,int* endPreorder,int* startInorder,int* endInorder){
	int rootValue = startPreorder[0];
	Node* root = new Node();
	root->value = rootValue;
	root->leftNode = root->rightNode = NULL;
	//递归停止条件，只有一个节点就返回根节点
	if(startPreorder == endPreorder){
		if(startInorder == endInorder&&*startPreorder==*startInorder)
			return root;
		else
			throw std::exception("invaild input");
	}
	int *rootInorder = startInorder;
	while(rootInorder<=endInorder&&*rootInorder!=rootValue)
		++rootInorder;
	if(rootInorder == endInorder&& *rootInorder!=rootValue)
		throw std::exception("invaild input");
	int leftLength=rootInorder-startInorder;
	int* leftPreorderEnd = startPreorder +leftLength;
	//递归停止条件之左子树或右子树为0，该树不返回该树
	if(leftLength>0){
		root->leftNode = ConstructCore(startPreorder+1,leftPreorderEnd,startInorder,rootInorder-1);	
	}
	if(leftLength<endPreorder-startPreorder){
		root->rightNode = ConstructCore(leftPreorderEnd+1,endPreorder,rootInorder+1,endInorder);	
	}
	return root;


}

Node* Construct(int *preorder,int *inorder,int length)
{
	if(preorder == NULL||inorder==NULL||length<=0)
		return NULL;
	return ConstructCore(preorder,preorder+length-1,inorder,inorder+length-1);
}
void main(){
	int pre[] = {1,2,3,4};
	int in[] = {4,3,2,1};
	Node*tree = Construct(pre,in,3);
	cout<<tree->value;
	cout<<tree->leftNode->value;
	int p;
	cin>>p;



}