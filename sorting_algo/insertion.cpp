/*
 * insertion.cpp
 * 
 * Copyright 2015 Anurag Singh
 * anurag.ull@gmail.com
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
 
 // project include 
 #include "insertion.h"
 // system include
#include <iostream>

template <class T>
void insertsort<T>::runInsertSort(T * arr,int size) {
	
	std::cout << "starting insertion sort \n";
	// outer loop
	for(int i =1 ; i< size ; i++ ) {
		// inner loop 
		int j = i;		
		while(arr[j] < arr[j-1]  && j > 0) {
			std::swap(arr[j],arr[j-1]);
			j--;
		}		
	}
}

template <class T>
void insertsort<T>::runInsertSort(std::vector<T> & vec){
	
	std::cout << "starting insertion sort \n";
	// outer loop
	for(int i =1 ; i< vec.size() ; i++ ) {
		// inner loop 
		int j = i;		
		while(vec[j] < vec[j-1]  && j > 0) {
			std::swap(vec[j],vec[j-1]);
			j--;
		}		
	}
}



