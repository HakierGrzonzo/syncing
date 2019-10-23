#include<string>
#include<tuple>
#include<iostream>
#include<exception>
#include<vector>
#include<algorithm>
using namespace std;

class Odcinek {
	public:
		int length;
		Odcinek(int _length){
			length = _length;
		}
		Odcinek(){
			length = 0;
		}
		tuple<Odcinek,Odcinek> Divide(int newLength){
			if(length > newLength){
				return make_tuple(Odcinek(newLength), Odcinek(length - newLength));
			}
			else{
				throw 1;
			}
		}
		bool operator<(const Odcinek & other){
			return length < other.length;
		}
};

Odcinek Glue(Odcinek x, Odcinek y){
	return Odcinek(x.length + y.length);
}



int main(){
	int num;
	int targetLength;
	int givenLength;
	cin >> num >> targetLength >> givenLength;
	vector<Odcinek> scraps;
	int made = 0;
	int cuting = 0;
	int used = 0;
	Odcinek basePlank = Odcinek(givenLength);
	while(made != num){
		Odcinek making = Odcinek(0);
		while(true){
			if(making.length < targetLength){
				if(targetLength - making.length >= making.length){
					//clog << "Attempting to Glue new plank\n";
					making = Glue(making, basePlank);
					used++;
				}
				else{
					if(scraps.empty()){
						//clog << "Attempting to cut new plank\n";
						int requiredLength = targetLength - making.length;
						Odcinek scrap1;
						Odcinek scrap2;
						//clog << "cuting\n";
						tie(scrap1, scrap2) = basePlank.Divide(requiredLength);
						making = Glue(making, scrap1);
						used++;
						cuting++;
						//clog << "adding to a pile\n";
						scraps.push_back(scrap2);
					}
					else{
						Odcinek					
					}
				}
			}
			else{
				cout << "ToDo";
			}

			if(making.length == targetLength){
			       made++;
			       break;
			}
					
		}
	}
	cout << made << "\t" << cuting << "\t" << used << "\n";
	return 0;
}
