/*
 * knight.h
 * 
 * Copyright 2015 Anurag Singh <anurag.ull@ygmail.com>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */
#ifndef _knight_hpp_
#define _kinght_hpp_

// project headers if any

// system headers if any
#include <vector>
#include <queue>
#include <stack>
struct moves{
		int x;
		int y;
		moves(int x_,int y_):x(x_),y(y_){}
		moves(){}
	};
	

class knightBoard{
	
	public:
	// blank ctr
	knightBoard(); 
	
	~knightBoard();
	
	void setBoardDimensions(int width_, int height_);
	
	void initBoard();
	
	std::vector<moves> sequenceGenerator(int srcX, int srcY,int desX,int desY,int level);
	
	
	
	void initBoardLevel4();
	
	
	void printMoves(std::vector<moves> mvs);
	
	void printBoard();
	
	//std::vector getRandomMoves();
	
	bool validateMove(int oriX,int oriY,int newX, int newY);
	
	void validateSequence(std::vector<moves> seqMoves,bool printstatus =false);
	
	void setNeighbor(std::vector<moves> seqMoves,int oriX,int oriY);
	
	
	
	std::vector<moves> getValidMoves(int currentX_,int currentY_);	
	
	// helper function 
	void createKnightGraph( int **graph, int vertices);
	
	std::vector<moves> setValidMoves(int currentX_,int currentY_);
	
		
	void setneighbour(std::vector<moves> neigh, int **graph, int x, int y);
	
	void greedySearch(int **graph, int src, int dest,std::vector<moves> & seqMoves);
	
	// level 4
	std::vector<moves> setValidMovesLevel4(int currentX_,int currentY_);
	
	
	bool checkForLevel4(int oriX,int oriY,int newX, int newY);
	
	void  settoggle();
	
	private :
	 char *boardChar;
	 char *startLabel;
	 char *endLabel;
	 char *currentLabel;
	 unsigned int width;
	 unsigned int height;
	 int CurrentPositionX;
	 int CurrentPositionY;
	 int toggleX[2];
	 int toggleY[2];
	 std::queue<int> myqueue;
	 void getToggle(int &x , int &y);
};

#endif


