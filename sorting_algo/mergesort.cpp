/*
 * mergesort.h
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
#include "mergesort.h"
 // system include
#include <iostream>
#include <algorithm>
#include <queue>  

template<class Iter>
void merge_sort(Iter begin, Iter end) {
	
	 int size = end - begin;
	 if(size > 1) {
	 
	 Iter midSize = begin+ size/2;
	 merge_sort(begin,midSize);
	 merge_sort(midSize, end);
	 std::inplace_merge(begin,midSize,end); 
 }
}
template<class T>
void merge(T * arr,int low,int middle,int high) {
	// two priority queus
	
	 std::priority_queue<T> pq1;
	 std::priority_queue<T> pq2;
	 
	 // store from low to middle in first 
	 for(int i=0; i< middle ; i++ ) {pq1.push(arr[i]);}
	 
	 for(int i=middle; i< high ; i++ ) {pq2.push(arr[i]);}
	// std::cout << pq1.size() << "\t" << pq2.size() << "\n";
	 int count = high-1; 
	 while(count >= 0) {
	//	 std::cout << pq1.size() << "\t" << pq2.size() << "\n";
		 if(!pq1.empty() && pq1.top() > pq2.top()) {
			 arr[count] =  pq1.top() ;
			 pq1.pop();
			 count--;
			 
		}else if(!pq2.empty()){
			arr[count] =  pq2.top() ;
			 pq2.pop();
			 count--;
		}
		else if(!pq1.empty() && pq2.empty()) {
			arr[count] =  pq1.top() ;
			 pq1.pop();
			 count--;
		} else if(!pq2.empty() && pq1.empty()) {
			arr[count] =  pq2.top() ;
			 pq2.pop();
			 count--;
		}
		 
	 }
}

 
 template <class T>
void mergesort<T>::runMergeSort(T * arr,int low,int high) {
	std::cout << "starting insertion sort \n";
	int middle;
	
	if(low < high){
		middle = (low+high)/2;
		runMergeSort(arr,low,middle);
		runMergeSort(arr,middle+1,high);
		merge(arr,low,middle,high);		
	}
	
}
template <class T>
 void mergesort<T>::runMergeSort(std::vector<T> & vec) {
	 std::cout << "starting merge sort \n";
	 merge_sort(vec.begin(),vec.end());
 }
