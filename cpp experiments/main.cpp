#include <iostream>
#include <string>
using namespace std;

long silnia(long num){
	long res;
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
void prlongNum(long num){
	string str = to_string(num);
	if(num > 0){
		long polong = str.size() - 1;
		while(true){
			if(str.at(polong) == '0'){
				polong--;	
			}
			else{
				break;
			}
		}
		cout << str.at(polong) << "\n";
	}
}


int main(){
	for(int i = 1; i < 95; i++){
		long duze = silnia(i);
		cout << "basenum: " << duze << "\t";
		prlongNum(duze);
	}
	return 0;
}
