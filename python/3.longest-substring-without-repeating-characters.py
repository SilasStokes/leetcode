#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_index = {}
        length = 0
        start = 0
        # "pwwkew" -> { p : 0 , w : 2 , k : 3 , e : 4  }
        # l = 3
        # s = 3
        for i, c in enumerate(s):
            if c in last_seen_index and last_seen_index[c] >= start:
                start = last_seen_index[c] + 1 # abca ->bca

            length = max(length, i - start + 1)
            last_seen_index[c] = i

        return length


        
# @lc code=end


    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) == 1: return 1
    #     debug = s == "abcabcbb"
    #     # all ascii is 2^8
    #     ascii_table = [0] * 2**8
    #     length = 0
    #     cur_len = 0
    #     for c in s:
    #         cur_len += 1
    #         index = ord(c)
    #         ascii_table[index] += 1
    #         if debug: print("len: " + format(length) + " cur_len = " +format(cur_len) + ", c = " + format(c) + ", ascii[index] = " +format(ascii_table[index]))
    #         if ascii_table[index] == 2:
    #             ascii_table = [0] * 2**8
    #             length = max(length, cur_len -1)
    #             ascii_table[index] = 1
    #             cur_len = 1
    #     return length
                # clear ascii table
                