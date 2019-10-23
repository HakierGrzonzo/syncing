#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
/*
bool isPrime(int num){
	int m = num/2;
	bool result = true;
	for(int i = 2; i <=m; i++){
	       if(num % i == 0){
	       		result = false;
			break;
	       }
	}
	return result;
}       
*/
bool isPrime(int n) {

    if(n<=1)

        return false;



    if(n<=3)

        return true;



    if(n%2==0||n%3==0)

        return false;



    for(int i=5;i*i<=n;i=i+6) {

        if(n%i==0||n%(i+2)==0)

            return false;

    }
    return true;
}
int main(){
	int rows;
	int cols;
	cin >> rows >> cols;
	char data[rows][cols];
	for(int i = 0; i < rows; i++){
		cin >> data[i];
	}
	
	//iter over array
	int steps[rows];
       	for(int x = 0; x < rows; x++){
		steps[x] = 0;
	}

	vector<int> numbers;
	while(steps[0] < cols){
		for(int x = rows - 1; x != 0;x--){
			if(steps[x] == cols){
				steps[x] = 0;
				steps[x - 1]++;
			}
		}
		int working = 0;
		for(int x = 0; x < rows; x++){
			working = 10 * working + data[x][steps[x]] - '0';
		}
		numbers.push_back(working);
		//clog << "calculating for: " << working << "\n";
		steps[rows - 1]++;
	}
	numbers.pop_back();
	numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());
	numbers.erase(remove_if(numbers.begin(), numbers.end(), [](const int& x) { return not isPrime(x);}), numbers.end());
	cout << numbers.size();
	return 0;
}
