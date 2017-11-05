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
 
 
 #ifndef _merge_sort_h_
 #define _merge_sort_h_
 
 #include <vector>
 
 template <class T>
 class mergesort{
	 
	public:
	 void runMergeSort(T * arr,int low,int high);
	 void runMergeSort(std::vector<T> & vec);
	 
 };
 
 #endif
