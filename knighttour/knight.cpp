/*
 * knight.cpp
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
 
// project headers if any
#include "knight.h"
#include "shortpath.h"
// system headers if any
#include <iostream> 	/* cout */
#include <stdlib.h>     /* abs */

struct node{
	int index;
	node *parent;
	};	

	knightBoard::knightBoard()
	:width(8), // default board
	height(8),
	CurrentPositionX(0),
	CurrentPositionY(0),
	startLabel(new char('S')),
	endLabel(new char('E')),
	currentLabel(new char('K'))
	{
	}
	
	knightBoard::~knightBoard(){
		
		for(unsigned int  i=0 ; i< width ; i++) {
		//	delete []boardDim[i];			
		
		}
	}


void knightBoard::setBoardDimensions( int width_, int height_) {
	// check  for size
	
	if(width_ < 1 || height_ < 1) {
		std::cout << "invalid size \n";
		return;
	}
	width = width_;
	height = height_;
}

void knightBoard::initBoard() {
	// check if height and width are greater than zero
	if(width < 1 || height < 1) {
		std::cout << " Dimensions should be greater than zero \n";
		return;
	}
	// initallize one dimension	
	//boardDim = new int*[width];
	boardChar = new char[width*height+1];
	for(unsigned int  i=0 ; i< width ; i++) {
		//boardDim[i] = new int[height];
		//boardChar[i] = new string [height];
	}
	
	for(unsigned int  i=0 ; i< width ; i++) {
		for(unsigned int  j=0 ; j< height ; j++) {
			boardChar[i*width+j] = '.';
		}
	}
	boardChar[width*height+1] = '\0';
}

void knightBoard::printBoard() {
	std::cout << "******** Printing Board ************ \n";
	std::cout << "\t";
	for(unsigned int  i=0 ; i< height ; i++) {
		std::cout << i << "\t";
	}
	std::cout << std::endl;
	for(unsigned int  i=0 ; i< width ; i++) {
		std::cout << i << "\t" ;
		for(unsigned int  j=0 ; j< height; j++) {
			std::cout  << boardChar[i*width+j] << "\t";
		}
		std::cout << std::endl;
	}
}

bool knightBoard::validateMove(int oriX,int oriY,int newX, int newY){
	// check if values are correct 
	if(oriX < 0 || oriX > width || oriY < 0 || oriY > height )
		return false;
	if(newX < 0 || newX > width || newY < 0 || newY > height )
		return false;
	
	int xDistance = abs(oriX - newX);
	int yDistance = abs(oriY - newY);
	
	if((xDistance*xDistance + yDistance*yDistance) == 5)
		return true;
	else
		return false; 
}



void knightBoard::setNeighbor(std::vector<moves> seqMoves,int oriX,int oriY) {
for(unsigned int  i=0 ; i< width ; i++) {
		for(unsigned int  j=0 ; j< width ; j++) {
			boardChar[i*width+j] = '.';
		}
	}
	boardChar[oriX*width+oriY] = 'O';
	for (std::vector<moves>::iterator it = seqMoves.begin() ; it != seqMoves.end(); ++it) {
		moves mv = *it;
		int newX = mv.x;
		int newY = mv.y;
		boardChar[newX*width+newY] = 'V';
	}
	
}

void knightBoard::validateSequence(std::vector<moves> seqMoves,bool printstatus = false) {
	// iterate over the board
	int countMoves =0;
	int lastPositionX = CurrentPositionX ;
	int lastPositionY = CurrentPositionY ;
	for (std::vector<moves>::iterator it = seqMoves.begin() ; it != seqMoves.end(); ++it) {
		moves mv = *it;
		int newX = mv.x;
		int newY = mv.y;
		bool checkMove = validateMove(CurrentPositionX,CurrentPositionY,newX,newY);
		if(checkMove == false) {
			continue;
		}
		// some temp variable for status check
		lastPositionX = CurrentPositionX ;
		lastPositionY = CurrentPositionY ;
		CurrentPositionX = newX;
		CurrentPositionY = newY;
		// check for the start condition
		if(countMoves == 0) {
			boardChar[CurrentPositionX*width+CurrentPositionY] = 'S';//startLabel;			
		}
		else{
			boardChar[CurrentPositionX*width+CurrentPositionY] = 'K';//currentLabel;
			if(countMoves > 1)
			boardChar[lastPositionX*width+lastPositionY] = '.';
		}
			countMoves++;
			//print board
			if(printstatus == true) {
				printBoard();
			}
	}
	// end status
	boardChar[CurrentPositionX*width+CurrentPositionY] = 'E';//endLabel;
	printBoard();
}

std::vector<moves> knightBoard::setValidMoves(int currentX_,int currentY_) {
	
	std::vector<moves> posibleMoves;
	// there are eight possible moves 
	int xValues[4] = {2,1,-1,-2};
	int yValues[4] = {2,1,-1,-2};
	
	moves nextMove; 
	
	
	for(int i = 0; i < 4 ; i++ ) {
		for(int j= 0 ; j < 4 ; j++ ) {
			if(abs(xValues[i]) != abs(yValues[j])) {
				nextMove.x = currentX_ - xValues[i];
				nextMove.y = currentY_ - yValues[j];
				// check for toggle 
				if(boardChar[CurrentPositionX*width+CurrentPositionY] = 'T');
				if(validateMove(currentX_,currentY_,nextMove.x,nextMove.y)) {
					posibleMoves.push_back(nextMove);
				}
			}
		}
	}
	
	
	return  posibleMoves;
	
}	

void knightBoard::createKnightGraph( int **graph, int vertices) {

	for(int i=0 ; i< vertices;i ++ ) {
		for(int j=0 ; j< vertices;j ++ ) {
			graph[i][j] = 0;
		}
	}
	
		
	for(int i=0 ; i< width;i ++ ) {
		for(int j=0 ; j< height;j++ ) {
				std::vector<moves> posibleMoves = setValidMoves(i,j); 
				setneighbour(posibleMoves,graph,i,j);
		}		
	}
	

}


void knightBoard::setneighbour(std::vector<moves> neigh, int **graph, int x, int y) {

	int position = x*width + y;
//	std::cout << position << "\tset neighbour \n";
	for (std::vector<moves>::iterator it = neigh.begin() ; it != neigh.end(); ++it) {
		moves mv = *it;
		int newX = mv.x;
		int newY = mv.y;
		int newPosition = newX*width+newY;
		// setWeigthts 
		char boardPos = boardChar[newPosition] ;
		int weightEdge = 0;
		switch(boardPos ) {
			case 'W':weightEdge  = 2;
			break;
			case 'L':weightEdge  = 5;
			break;
			//case 'R':
			//break;
			default : weightEdge  = 1;
			break;
			
		}
		
		
			graph[position][newPosition] = weightEdge ;
	
		//boardChar[newX*width+newY] = 'V';
	}

}


std::vector<moves> knightBoard::sequenceGenerator(int srcX, int srcY,int desX,int desY, int level) {
	std::vector<moves> seqMoves;
	
	int totalvertices = width*height;
	int **graph;
	
	graph = new int * [totalvertices];
	for(int i =0 ; i < totalvertices ; i++ ) {
		graph[i] = new int[totalvertices];
	}
	
	
	createKnightGraph(graph, totalvertices);
	
	int src =  srcX*width + srcY;
	int des = desX*width +  desY;
	
	shortPath sp;
	sp.setNumOfVertice(totalvertices);
	std::stack<int> val ;
	
	// switch to choose between 2,3, or 5
	switch(level) {
		case 2: val = sp.greedySearch (graph,src,des);
		break ; 
		case 3: val = sp.dijkstra (graph,src,des);
		break ;
		case 5: val = sp.dijkstradriver (graph,src,des);
		break ;
	}
	
	while(!val.empty()) {
		int pos = val.top();
		int x = pos/width;
		int y = pos % width;
		seqMoves.push_back(moves(x,y));
		val.pop();
	}
	
	// clean up 
	
	delete graph;
	return seqMoves;
	
}
// level 4 ///


bool knightBoard::checkForLevel4(int oriX,int oriY,int newX, int newY) {
	// if its rock and blockade
	int position = newX * width +  newY;
	if(boardChar[position] == 'R' || boardChar[position] == 'B') {
		return false;
	}
	// check for blockade will be in middle of x or y 
	int middleX = 0;
	int middleY = 0;
	 if(abs(oriX - newX)%2 == 0) {
		 middleX = (oriX + newX)/2;
		 middleY = oriY; 
	 }
	 else {
		 middleX = oriX;
		 middleY = (oriY + newY)/2; 
	 }
	 position =  middleX * width +  middleY;
	 if(boardChar[position] == 'B') {
		return false;
	 }
	 return true;
	
}


std::vector<moves> knightBoard::setValidMovesLevel4(int currentX_,int currentY_) {
	
	std::vector<moves> posibleMoves;
	// there are eight possible moves 
	int xValues[4] = {2,1,-1,-2};
	int yValues[4] = {2,1,-1,-2};
	
	moves nextMove; 
	
	
	for(int i = 0; i < 4 ; i++ ) {
		for(int j= 0 ; j < 4 ; j++ ) {
			if(abs(xValues[i]) != abs(yValues[j])) {
				nextMove.x = currentX_ - xValues[i];
				nextMove.y = currentY_ - yValues[j];
				// check for toggle
				if(boardChar[nextMove.x*width+nextMove.y] == 'T') {
					getToggle(nextMove.x , nextMove.y );
				}
				
				if(validateMove(currentX_,currentY_,nextMove.x,nextMove.y) 
					&& checkForLevel4(currentX_,currentY_,nextMove.x,nextMove.y))
					posibleMoves.push_back(nextMove);
			}		
		
		}
		
	}
	
	
	return  posibleMoves;
	
}	

void knightBoard::settoggle(){
	int count =0 ;
	for(unsigned int  i=0 ; i< width ; i++) {
		for(unsigned int  j=0 ; j< height ; j++) {
			if(boardChar[i*width+j] == 'T') {
				toggleX[count] = i;
				toggleY[count] = j;
				count++;
				if(count > 1)
					return;
			}			
		}		
	}
	
}
// function for toggle

void knightBoard::getToggle(int &x , int &y) {
	if(x == toggleX[0] && y == toggleY[0] ) {
		x = toggleX[1];
		y = toggleY[1];		
	}
	else{
		x = toggleX[0];
		y = toggleY[0];	
	}		
}
/*
void knightBoard::createKnightGraphLevel4( int **graph, int vertices) {

	for(int i=0 ; i< vertices;i ++ ) {
		for(int j=0 ; j< vertices;j ++ ) {
			graph[i][j] = 0;
		}
	}
	
		
	for(int i=0 ; i< width;i ++ ) {
		for(int j=0 ; j< height;j++ ) {
				std::vector<moves> posibleMoves = setValidMoves(i,j); 
				setneighbour(posibleMoves,graph,i,j);
		}		
	}
	

}

*/

void knightBoard::initBoardLevel4() {
		
	char broad2[] = {'.','.','.','.','.','.','.','.','B','.','.','.','L','L','L','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','.','.','.','L','L','L','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','.','.','.','L','L','L','.','.','.','L','L','L','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','.','.','.','L','L','L','.','.','L','L','L','.','.','.','R','R','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','.','.','.','L','L','L','L','L','L','L','L','.','.','.','R','R','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','.','.','.','L','L','L','L','L','L','.','.','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','B','B','.','.','.','.','.','.','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','W','B','B','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','R','R','.','.','.','W','W','B','B','B','B','B','B','B','B','B','B','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','R','R','.','.','.','W','W','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','W','W','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','T','.','.','.','.','.',
'.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','.','.','.','.','B','.','.','R','R','.','.','.','.','.','.','.','.',
'.','.','.','W','W','.','.','.','.','.','.','.','.','.','.','B','B','B','B','B','.','.','R','R','.','W','W','W','W','W','W','W',
'.','.','.','W','W','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','W','.','.','.','.','.','.',
'W','W','W','W','.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','.',
'.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','.','.','B','B','B','B',
'.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','B','B','B','.','.','.','.','.','.','.','.','.','.','B','.','.','.',
'.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','.','.','B','W','W','W','W','W','W','B','B','B','B','B','.','.','.',
'.','.','.','W','W','W','W','W','W','W','.','.','.','.','.','.','.','B','W','W','W','W','W','W','B','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','B','B','.','.','.','.','.','.','.','.','.','.','B','B','.','.','.','.','.','.',
'.','.','.','.','.','R','R','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.',
'.','.','.','.','.','R','R','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','.','.','.','B','.','T','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','R','R','.','.','.','.','.','.','B','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','R','R','.','.','.','.','.','.','B','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.',
'.','.','.','.','.','.','.','.','.','.','.','B','.','.','.','.','.','.','.','.','.','.','R','R','.','.','.','.','.','.','.','.',
'\0'};

	for(unsigned int  i=0 ; i< width ; i++) {
		for(unsigned int  j=0 ; j< height ; j++) {
			boardChar[i*width+j] = broad2[i*width+j];		
		}
	}	
}


