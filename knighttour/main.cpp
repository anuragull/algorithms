/*
 * main.cpp
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
// system headers if any
#include <iostream>



void testLevels(knightBoard k1,int srcX, int srcY,int desX,int desY,int option);

void runTest(int val);
int main(int argc, char **argv)
{
	
	for(int i=1;i < 5 ; ++i)
		runTest(i);
	
	return 0;
}


void runTest(int val) {
	knightBoard k1,k2;
	k1.setBoardDimensions(8,8);
	k1.initBoard();
	std::vector<moves> seqMoves;
	
	// set some random points
	moves mv1(2,1);
	seqMoves.push_back(mv1);
	moves mv2 (4,2);
	seqMoves.push_back(mv2);
	moves mv3 (7,4);
	seqMoves.push_back(mv3);
	moves mv4 (6,3);
	seqMoves.push_back(mv4);
	moves mv5 (5,5);
	seqMoves.push_back(mv5);
	
	
	k2.setBoardDimensions(32,32);
	k2.initBoard();
	k2.initBoardLevel4() ;
	
	switch(val) {
		
		case 1 : k1.validateSequence(seqMoves,true);
		break; 
		case 2 : testLevels(k1,2,1,5,5,val);
		break; 
		case 3 : testLevels(k1,2,1,5,5,val);
		break;
		case 4 : testLevels(k2,0,0,31,30,3);
		break;
		case 5 : testLevels(k2,0,0,31,30,val);
		break;
		
	}
	
	
}


void testLevels(knightBoard k1,int srcX, int srcY,int desX,int desY,int option) {
	std::vector<moves> sp = k1.sequenceGenerator(srcX,  srcY, desX, desY,option) ;
	k1.validateSequence(sp,true);
	
}


