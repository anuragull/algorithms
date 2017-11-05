/*
 * quicksort.cpp
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
#include "quicksort.h"
 // system include
#include <iostream>
#include <algorithm>

template <class T>
int partition(T * arr, int low, int high) {
	int firstHigh=low;
	
	for(int i=low; i < high ; i++) {
		
		if(arr[i] < arr[high]) {
			std::swap(arr[i],arr[firstHigh]);
			firstHigh++;			
		}
	}
	std::swap(arr[high],arr[firstHigh]);
	
	return firstHigh;
}


template<class Iter>
void quick_sort(Iter begin, Iter end) {
	
	 int size = end - begin;
	 if(size > 1) {
	 
	 
	 Iter midSize = begin+ size/2;
	 std::nth_element (begin, midSize, end);
	 quick_sort(begin,midSize);
	 quick_sort(midSize, end);
 }
}

 template <class T> 
  void quicksort<T>::runQuickSort(T * arr,int low,int high) {
	  int p ; 
	  if((high - low) > 0 ) {
		  p = partition(arr,low,high);
		  runQuickSort(arr,low,p-1);
		  runQuickSort(arr,p+1,high);
	  }
  }
  
  template <class T> 
  void quicksort<T>::runQuickSort(std::vector<T> & vec) {
	   std::cout << "starting quick sort \n";
	quick_sort(vec.begin(),vec.end());
  }
