--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--
-- https://leetcode.com/problems/combine-two-tables/description/
--
-- database
-- Easy (73.78%)
-- Likes:    2941
-- Dislikes: 212
-- Total Accepted:    788.5K
-- Total Submissions: 1.1M
-- Testcase Example:  '{"headers":{"Person":["personId","lastName","firstName"],"Address":["addressId","personId","city","state"]},"rows":{"Person":[[1,"Wang","Allen"],[2,"Alice","Bob"]],"Address":[[1,2,"New York City","New York"],[2,3,"Leetcode","California"]]}}'
--
-- Table: Person
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
-- personId is the primary key column for this table.
-- This table contains information about the ID of some persons and their first
-- and last names.
-- 
-- 
-- 
-- 
-- Table: Address
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
-- addressId is the primary key column for this table.
-- Each row of this table contains information about the city and state of one
-- person with ID = PersonId.
-- 
-- 
-- 
-- 
-- Write an SQL query to report the first name, last name, city, and state of
-- each person in the Person table. If the address of a personId is not present
-- in the Address table, report null instead.
-- 
-- Return the result table in any order.
-- 
-- The query result format is in the following example.
-- 
-- 
-- Example 1:
-- 
-- 
-- Input: 
-- Person table:
-- +----------+----------+-----------+
-- | personId | lastName | firstName |
-- +----------+----------+-----------+
-- | 1        | Wang     | Allen     |
-- | 2        | Alice    | Bob       |
-- +----------+----------+-----------+
-- Address table:
-- +-----------+----------+---------------+------------+
-- | addressId | personId | city          | state      |
-- +-----------+----------+---------------+------------+
-- | 1         | 2        | New York City | New York   |
-- | 2         | 3        | Leetcode      | California |
-- +-----------+----------+---------------+------------+
-- Output: 
-- +-----------+----------+---------------+----------+
-- | firstName | lastName | city          | state    |
-- +-----------+----------+---------------+----------+
-- | Allen     | Wang     | Null          | Null     |
-- | Bob       | Alice    | New York City | New York |
-- +-----------+----------+---------------+----------+
-- Explanation: 
-- There is no address in the address table for the personId = 1 so we return
-- null in their city and state.
-- addressId = 1 contains information about the address of personId = 2.
-- 
-- 
--
-- SELECT p.firstName,p.lastName,a.city,a.state 
-- FROM Person as P 
-- LEFT JOIN 
--     Address as a on p.personId=a.personId;

-- @lc code=start
# Write your MySQL query statement below
SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM
    Person
LEFT JOIN 
    Address 
ON 
    Person.personId = Address.personId;

-- @lc code=end

