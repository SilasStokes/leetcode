#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (35.89%)
# Likes:    2711
# Dislikes: 351
# Total Accepted:    110.5K
# Total Submissions: 299.6K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
  # '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in
# the user's news feed.
# 
# Implement the Twitter class:
# 
# 
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
# by the user userId. Each call to this function will be made with a unique
# tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
# in the user's news feed. Each item in the news feed must be posted by users
# who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed",
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
# 
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2
# tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is
# posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5], since user 1 is no longer following user 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
# unfollow.
# 
# 
#
from typing import List
import heapq

# @lc code=start
class Twitter:
    def __init__(self):
        self.users = {}
        self.heap = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users.keys():
            self.users[userId] = {'followers' : [], 'following' : [], 'tweets' : [], 'newsfeed' : []}
        
        self.users[userId]['tweets'].append( (self.time, tweetId, userId))
        heapq.heappush(self.users[userId]['newsfeed'], (self.time, tweetId, userId))
        for follower in self.users[userId]['followers']:
            heapq.heappush(self.users[follower]['newsfeed'], (self.time, tweetId, userId))

        # heap = self.users[userId]['newsfeed']
        # print(f'Current heap: {heap}')
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users.keys():
            self.users[userId] = {'followers' : [], 'following' : [], 'tweets' : [], 'newsfeed' : []}

        num_smallest = 10 if len(self.users[userId]['newsfeed']) >10 else len(self.users[userId]['newsfeed'])

        return [ tweet for _,tweet,_ in heapq.nsmallest(num_smallest, self.users[userId]['newsfeed']) ]
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId started following the user with ID followeeId.
        """
        if followerId not in self.users.keys():
            self.users[followerId] = {'followers' : [], 'following' : [], 'tweets' : [], 'newsfeed' : []}
        if followeeId not in self.users.keys():
            self.users[followeeId] = {'followers' : [], 'following' : [], 'tweets' : [], 'newsfeed' : []}

        if followeeId in self.users[followerId]['following']:
            return

        self.users[followeeId]['followers'].append(followerId)

        self.users[followerId]['following'].append(followeeId)
        # add tweets from followee to followerID
        for tweet in self.users[followeeId]['tweets']:
            heapq.heappush(self.users[followerId]['newsfeed'], tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        '''
        The user with ID followerId started unfollowing the user with ID followeeId.
        '''
        if followerId not in self.users.keys():
            self.users[followerId] = {'followers' : [], 'following' : [], 'tweets' : [], 'newsfeed' : []}
        if followeeId not in self.users.keys():
            self.users[followeeId] = {'followers' : [], 'following' : [], 'tweets' : [], 'newsfeed' : []}

        if followeeId not in self.users[followerId]['following']:
            return

        self.users[followerId]['following'].remove(followeeId)
        self.users[followeeId]['followers'].remove(followerId)
        i = 0
        while i < len(self.users[followerId]['newsfeed']):
            timestamp, tweetId, userId =self.users[followerId]['newsfeed'][i]
            if userId == followeeId: # remove it
                del self.users[followerId]['newsfeed'][i]
                i -= 1

            i += 1
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

