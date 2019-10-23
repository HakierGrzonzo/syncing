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
				if(targetLength - making.length >= basePlank.length){
					if(scraps.empty()){
						//clog << "Attempting to Glue new plank\n";
						making = Glue(making, basePlank);
						used++;
					}
					else{
						//clog << "making use of scraps\n";
						Odcinek small = *min_element(scraps.begin(), scraps.end());
						scraps.erase(min_element(scraps.begin(), scraps.end()));	
						if(small.length + making.length <= targetLength){
							making = Glue(making, small);
						}
						else{
							int requiredLength = targetLength - making.length;
							Odcinek scrap1;
							Odcinek scrap2;
							tie(scrap1, scrap2) = small.Divide(requiredLength);
							cuting++;
							scraps.push_back(scrap2);
							making = Glue(making, scrap1);
						}
					}
				}
				else{
					if(scraps.empty()){
						//clog << "Attempting to cut new plank\n";
						int requiredLength = targetLength - making.length;
						Odcinek scrap1;
						Odcinek scrap2;
						tie(scrap1, scrap2) = basePlank.Divide(requiredLength);
						making = Glue(making, scrap1);
						used++;
						cuting++;
						scraps.push_back(scrap2);
					}
					else{
						//clog << "making use of scraps\n";
						Odcinek small = *min_element(scraps.begin(), scraps.end());
						scraps.erase(min_element(scraps.begin(), scraps.end()));	
						if(small.length + making.length <= targetLength){
							making = Glue(making, small);
						}
						else{
							int requiredLength = targetLength - making.length;
							Odcinek scrap1;
							Odcinek scrap2;
							tie(scrap1, scrap2) = small.Divide(requiredLength);
							cuting++;
							scraps.push_back(scrap2);
							making = Glue(making, scrap1);
						}					
					}
				}
			}
			else{
				throw 69;
			}
			//clog << "current plank length: " << making.length << "\n";
			if(making.length == targetLength){
			       made++;
			       //cout << "\n";
			       break;
			}		
		}
	}
	//cout << made << "\t" << cuting << "\t" << used << "\n";
	cout << cuting;
	return 0;
}
