#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node: return node
        
#         clones = {}
#         clones[node.val] = Node(node.val, [])
#         q = deque([node])
#         while q:
#             cur = q.popleft() 
#             cur_clone = clones[cur.val]            

#             for ngbr in cur.neighbors:
#                 if ngbr.val not in clones:
#                     clones[ngbr.val] = Node(ngbr.val, [])
#                     q.append(ngbr)
                    
#                 cur_clone.neighbors.append(clones[ngbr.val])
                
#         return clones[node.val]


# BFS
from queue import Queue

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        visited_list = {}
        visited_list[node] = Node(node.val)

        q = Queue()
        q.put(node)

        while not q.empty():
            temp = q.get()
            clone_node = visited_list[temp]
            for neighbor in temp.neighbors:
                if neighbor not in visited_list:
                    visited_list[neighbor] = Node(neighbor.val)
                    q.put(neighbor)
                clone_node.neighbors.append(visited_list[neighbor])
            
        return visited_list[node]
        
# @lc code=end

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         oldToNew = {}
        
#         def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]
            
#             copy = Node(node.val)
#             oldToNew[node] = copy
#             for nei in node.neighbors:
#                 copy.neighbors.append(dfs(nei))
#             return copy
        
#         return dfs(node) if node else None

# To solve this problem we need two things:

# BFS to traverse the graph
# A hash map to keep track of already visited and already cloned nodes
# We push a node in the queue and make sure that the node is already cloned. Then we process neighbors. If a neighbor is already cloned and visited, we just append it to the current clone neighbors list, otherwise, we clone it first and append it to the queue to make sure that we can visit it in the next tick.

# Time: O(V + E) - for BFS
# Space: O(V) - for the hashmap

# Runtime: 32 ms, faster than 98.18% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.4 MB, less than 91.72% of Python3 online submissions for Clone Graph.
