#include<iostream>
#include<vector>
#include<tuple>
using namespace std;

class Board {
	public:
		int size;
		Tower *board[size][size];
		Board(int _size){
			size = _size;
			for(int i = 0; i < size; i++){
				for(int j = 0; j < size; j++){
					self[i][j] = Tower(i, j, *this);
				}
			}
		}
};

class Tower {
	public:
		bool isTower;
		Board *plansza;
		unsigned short int posX;
		unsigned short int posY;
		Tower(unsigned short int _posX, unsigned short int _posY, Board *_plansza){
			posX = _posX;
			posY = _posY;
			plansza = _plansza;
			isTower = false;
		}
		vector<Tower> Look(){
			vector<*Tower> res;
			for(unsigned short int x = posX + 1; x < (*plansza).size; x++){
				if((*plansza).(*board[x][posY]).isTower){
					res.push_back((*plansza).board[x][posY];
					break;
				}
			}
			for(unsigned short int x = posX - 1; x >= 0 ; x--){
				if((*plansza).(*board[x][posY]).isTower){
					res.push_back((*plansza).board[x][posY];
					break;
				}
			}
			for(unsigned short int y = posX - 1; y >= 0 ; y--){
				if((*plansza).(*board[posX][y]).isTower){
					res.push_back((*plansza).board[posX][y]);
					break;
				}
			}


};
