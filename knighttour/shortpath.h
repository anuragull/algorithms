/*
 * shortpath.h
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

#ifndef _shortpath_hpp_
#define _shortpath_hpp_

// system headers 
#include <stack>
#include <queue>



class shortPath {
	public:
	shortPath();
	
	~shortPath();
	
	void setNumOfVertice(int vert);
	
	int minDistance(int dist[], bool visitedNode[]) ;
	
	int maxDistance(int dist[], bool visitedNode[]);
	
	
	std::stack<int>  dijkstra(int **graph,  int src, int dest);
	
	void dijkstraMax(int **graph, int src,int dist[],int previous[]);
	
	std::stack<int> dijkstradriver(int **graph, int src, int dest) ;
	
	std::stack<int> greedySearch(int **graph, int src, int dest) ;
	
	private :
	int vertices;
	int *dist;
	int *previous;
	std::queue<int> myqueue;
	
	void setEveryElement(int elemArray[], int value) ;
};

#endif

