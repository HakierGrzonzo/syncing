#include <iostream>
#include <string>
using namespace std;

int silnia(int num){
	int res;
	if(num == 0){
		res = 1;
	}
	else if(num < 0){
		res = -1;
	}
	else{
		res = num*silnia(num-1);
	}

	return res;
}

int getLast(int num){
	if(num == 0){
		return 0;
	}
	else{
		while(true){
			int x = num % 10;
			if(x == 0){
				num = num/10;
			}
			else{
				return x;
				break;
			}
		}
	}
}

int impSilnia(int num){
	int acc = 1;
	for(int x = 1; x < num; x++){
		acc = getLast( acc * getLast(num));
	}
	return acc;
}

bool tester(int num){
	return getLast(silnia(num)) == impSilnia(num); 
}

int main(){
	for(int i = 1; i < 20; i++){
		int duze = impSilnia(i);
		cout << "basenum: " << i << "\t" << "duze: " << duze << "\n";
		//cout << "test " << i << "\t" << tester(i) << "\n"; 
	}
	return 0;
}
