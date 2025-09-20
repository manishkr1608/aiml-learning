"""
Course Schedule - LeetCode #207
Determine if you can finish all courses given prerequisites (topological sort).
"""

from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    visited = 0

    while q:
        node = q.popleft()
        visited += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return visited == numCourses

# Tests
print(can_finish(2, [[1,0]]))          # True
print(can_finish(2, [[1,0],[0,1]]))    # False
