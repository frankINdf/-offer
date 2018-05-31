#include<iostream>
#include<math.h>
#include<iomanip>
using namespace std;
bool g_InvalidInput = false;
double powWithUnsiged(double base,unsigned int exponent)
{
	double result = 1.0;
	while(exponent>0){
		result *=base;
		exponent--;
	
	}
	return result;

}
bool equal(double a,double b){
	if(fabs(a-b)<1e-3)
		return true;
	return false;
}

double power(double base,unsigned int exponent)
{
	g_InvalidInput = false;
	if(equal(base,0)&&exponent<0){
		g_InvalidInput = true;
		return 0.0;	
	}
	unsigned int absExponent = (unsigned int) exponent;
	if(exponent<0){
		absExponent = 	(unsigned int )(-exponent);
	}
	double result = powWithUnsiged(base,absExponent);
	if(exponent<0){
		result = 1.0/result;	
	}
	return result;

}


void main(){
	double f=1.5;
	double k=fabs(f);
	f=power(4.3,2);

	cout<<f;

	int s;
	cin>>s;
}