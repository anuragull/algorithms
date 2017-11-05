/*
 * shortpath.cpp
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

#include "shortpath.h"
// system headers if any
#include <queue>
#include <limits.h>   /* int max*/
#include <iostream>
struct node{
	int index;
	//std::vector<node*> children;
	node *parent;
	};	

shortPath::shortPath() {}

shortPath::~shortPath() {
	delete  dist;
	delete  previous;
	}




void shortPath::setNumOfVertice(int vert) {
	vertices= vert;
	dist = new int[vert];
	previous = new int[vert];
}

int shortPath::minDistance(int dist[], bool visitedNode[]){
	 // Initialize 
	 int min = INT_MAX, minIndex;
	 
	 for (int v = 0; v < vertices; v++)
		 if (visitedNode[v] == false && dist[v] <= min)
			 min = dist[v], minIndex = v;
	 
	 return minIndex;
}


int shortPath::maxDistance(int dist[], bool visitedNode[]) {
	// Initialize 
	int maxValue = -INT_MAX, maxIndex;
	
	for (int v = 0; v < vertices; v++)
		if (visitedNode[v] == false == false && dist[v] >= maxValue)
			maxValue = dist[v], maxIndex = v;
	
	return maxIndex;
	
}

std::stack<int>  shortPath::dijkstra(int **graph, int src, int dest) {
		
	// set visted nodes
	bool visitedNode[vertices]; 
	
	for (int i = 0; i < vertices; i++)
		dist[i] = INT_MAX, visitedNode[i] = false;
	
	// Distance of source vertex from itself is always 0
	dist[src] = 0;
	
	// Find shortest path for all vertices
	for (int count = 0; count < vertices-1; count++)
	{
		// get the minimun distance
		int u = minDistance(dist, visitedNode);
		// Set visited vertex as visited
		visitedNode[u] = true;
		// Update dist value of the adjacent vertices of the picked vertex.
		for (int v = 0; v < vertices; v++) {
			if (!visitedNode[v] && graph[u][v] && dist[u] != INT_MAX && dist[u]+graph[u][v] < dist[v]) {
				dist[v] = dist[u] + graph[u][v];
				previous[v]  = u; }
		}
	}
	// create a stack 
	std::stack<int> pathstack;
	int position = dest;
	while(position != src) {
		pathstack.push(position);
		position = previous[position];
	}
	pathstack.push(src);
	return pathstack;
}

std::stack<int> shortPath::greedySearch(int **graph, int src, int dest) {
	
	
	node * nodes[ vertices]; 
	for(int i=0; i <  vertices ; i++) {
			nodes[i] = new node();
			nodes[i]->index = i;
			nodes[i]->parent = 0;
	}
	
		
	int i=0;
	int pos; 
	
	std::queue<int> myqueue;
	myqueue.push(src);
	while(pos !=dest) {
		// add a queue 
		
		pos =  myqueue.front();
		for(int i=0; i <  vertices ; i++) {
			
			if(graph[pos][i] == 1) {
				if(i==src)
					continue;
				myqueue.push(i);
				if(	nodes[i]->parent == 0 )		
					nodes[i]->parent = 	nodes[pos];			
			}
		}		
		myqueue.pop();
	}
	
	node * tempNode = nodes[dest];
	std::stack<int> pathstack;
	
	while(tempNode->parent !=0 ) {
		pathstack.push(tempNode->index);
		tempNode = tempNode->parent;
	}
    
	// clean up 
	for(int i=0; i < vertices ; i++) {
			delete nodes[i] ;
	}
	return pathstack;
	
}


void shortPath::dijkstraMax(int **graph, int src,int dist[],int previousNode[]) {
	
	 bool visitedNode[ vertices];
	for (int i = 0; i < vertices; i++)
		dist[i] = -INT_MAX,  visitedNode[i] = false, previousNode[i] = -1;
	
	// Distance of source vertex from itself is always 0
	dist[src] = 0;
	
	// Find longest path for all vertices
	for (int count = 0; count < vertices-1; count++)
	{
		// get the minimun distance
		int u = maxDistance(dist, visitedNode);
		
		// Set visited vertex as visited
		visitedNode[u] = true;
		int index , value;
		// Update dist value of the adjacent vertices of the picked vertex.
		for (int v = 0; v < vertices; v++) {
		
		// if not visited and an edge and greater value
		if (!visitedNode[v] && graph[u][v] && dist[u] != -INT_MAX && dist[u]+graph[u][v] > dist[v]) {
		dist[v] = dist[u] + graph[u][v];
		previousNode[v]  = u; }
		}
	}
	
}

void shortPath::setEveryElement(int elemArray[], int value)  {
	for (int i = 0; i < vertices; i++) {
		elemArray[i] = value;
	}
}


std::stack<int> shortPath::dijkstradriver(int **graph, int src, int dest)  {
	

	                      
    int * previousNode  = new int[vertices];
   
     int **prevoiusNodeMatrix;
     int **dist2;
	
	prevoiusNodeMatrix 	= new int * [vertices];
    dist2				= new int * [vertices];;
   
    
    for(int i =0 ; i < vertices ; i++ ) {
		prevoiusNodeMatrix[i] 	= new int[vertices];
		dist2[i] 				= new int[vertices];
	}
     
    // initialize the values
	for (int i = 0; i < vertices; i++) {
		for (int j = 0; j< vertices; j++) {
			dist2[i][j] = 0;
			prevoiusNodeMatrix[i][j] = 0;
		}
	}
	// get longest path for all nodes from each source	
	for(int i = 0 ; i < vertices ; i++ ) {
		setEveryElement(dist,0);
		setEveryElement(previousNode,-1);
		dijkstraMax(graph,i,dist,previousNode);
		for (int j = 0; j< vertices; j++) {
			dist2[i][j] = dist[j];
			prevoiusNodeMatrix[i][j] = previousNode[j];
		}
	}
		
	
	// get the longest path from source to destination 
	std::stack<int> pathstack;
	std::stack<int> empty;
	int position = dest;
	int count =0;
	while(position != src) {
		count++; // variable for book keeping
		pathstack.push(position);	   
		position = prevoiusNodeMatrix[src][position];
		if(count > vertices) {
			return empty;
		}
	}
	// clean up 
	delete  previousNode;
	 for(int i =0 ; i < vertices ; i++ ) {
		delete prevoiusNodeMatrix[i];
		delete dist2[i]; 
	}
	return pathstack;
	
}


