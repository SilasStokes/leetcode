#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (40.49%)
# Likes:    15916
# Dislikes: 688
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
#

# @lc code=start
class LRUCache:
    class _Node:
        def __init__(self, val = 0, key = 0):
            self.prev, self.next = None, None
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        if capacity < 0:
            raise Exception('Invalid Capacity')
        self._cap = capacity
        self._cache = {}
        self._lru, self._mru = self._Node(), self._Node()
        self._lru.next = self._mru
        self._mru.prev = self._lru
    
    def _remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def _insert(self, node):
        pre, nxt = self._mru.prev, self._mru
        pre.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = pre

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._remove(self._cache[key])

        node = self._Node(value, key)
        self._cache[key] = node
        self._insert(node)

        if len(self._cache.keys()) > self._cap:
            lru = self._lru.next
            self._remove(lru)
            del self._cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

