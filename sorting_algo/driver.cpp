/*
 * driver.cpp
 * 
 * Copyright 2015 Anurag Singh
 * anurag.ull@gmail.com
 *  * 
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

// 
#include "insertion.h"
#include "insertion.cpp"
// system 
#include <iostream>

template <typename Type> 
void loadArray(Type * arry, int size) {
	int count = size;
	for(int i =0 ; i< size ; i++ ) {
		arry[i] = count;
		count --;
	}
}
template <typename Type> 
void printArray(Type * arry, int size) {
	for(int i =0 ; i< size ; i++ ) {
		std::cout << arry[i] << "\t";
	}
	std::cout << "\n";
}

template <typename Type> 
void loadVec(std::vector<Type> & vec,int size) {
	int count = size;
	for(int i =0 ; i< size ; i++ ) {
		vec.push_back(count);
		count --;
	}
}
template <typename Type> 
void printVec(std::vector<Type> & vec) {
	for(auto i : vec ) {
		std::cout << i << "\t";
	}
	std::cout << "\n";
}



int main(int argc, char **argv)
{
	insertsort<int> ins;
	
	
	int size = 10;
	int * arry= new int[size];
	std::vector<int> vec;
	loadArray<int>(arry,size);
	loadVec<int>(vec,size);
	
	printArray<int>(arry,size);
	ins.runInsertSort(arry,size);
	printArray<int>(arry,size);
	
	printVec<int>(vec);
	ins.runInsertSort(vec);
	printVec<int>(vec);
	delete arry;
	return 0;
}

