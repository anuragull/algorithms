"""
create a graph, 
create degrees for courses

Create a queue
edges, indegree. if no more depedency 
"""

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS and cycle 
        """
        
        edges = defaultdict(list)
        degrees = [0] * numCourses
        for course, pre_course in prerequisites:
            edges[pre_course].append(course)
            degrees[course] += 1

        queue = collections.deque(course for course, degree in enumerate(degrees) if not degree)
        
        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    queue.append(next_course)

        return not sum(degrees)
