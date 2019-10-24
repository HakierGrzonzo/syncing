#include<iostream>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;

int sum(int nums[], int size){
	int res = 0;
	for(int x = 0; x < size; x++){
		res = nums[x] + res;
	}
	return res;
}
bool helper(int* arr, int n, int start, int lsum, int rsum) 

{ 
    if (start == n){ 
        return lsum == rsum;
    }	
    else{
        return helper(arr, n, start + 1, lsum + arr[start], rsum) 
           || helper(arr, n, start + 1, lsum, rsum + arr[start]); 
    }
} 
bool splitArray(int* arr, int n) 
{ 
    return helper(arr, n, 0, 0, 0); 
} 

int main(){
	int SizeOfVals;
	cin >> SizeOfVals;
	int numbers[SizeOfVals];
	for(int x=0; x < SizeOfVals;x++){
		cin >> numbers[x];
	}
	int suma = sum(numbers, SizeOfVals);
	if(suma % 2 == 0 && SizeOfVals % 2 == 0){
		if(splitArray(numbers, SizeOfVals)){
			cout << "TAK";
		}
		else{
			cout << "NIE";
		}	
	}
	else{
		cout << "NIE";
	}
	return 0;


}
