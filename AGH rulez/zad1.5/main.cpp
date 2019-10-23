#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

int sum(int nums[], int size){
	int res = 0;
	for(int x = 0; x < size; x++){
		res = nums[x] + res;
	}
	return res;
}

int main(){
	int SizeOfVals;
	cin >> SizeOfVals;
	int numbers[SizeOfVals];
	for(int x=0; x < SizeOfVals;x++){
		cin >> numbers[x];
	}
	cout << sum(numbers, SizeOfVals) << "\n";
	return 0;
}
