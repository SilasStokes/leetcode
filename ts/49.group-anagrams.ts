/*
 * @lc app=leetcode id=49 lang=typescript
 *
 * [49] Group Anagrams
 *
 * https://leetcode.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (65.38%)
 * Likes:    11225
 * Dislikes: 360
 * Total Accepted:    1.5M
 * Total Submissions: 2.4M
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * Given an array of strings strs, group the anagrams together. You can return
 * the answer in any order.
 * 
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 * 
 * 
 * Example 1:
 * Input: strs = ["eat","tea","tan","ate","nat","bat"]
 * Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 * Example 2:
 * Input: strs = [""]
 * Output: [[""]]
 * Example 3:
 * Input: strs = ["a"]
 * Output: [["a"]]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= strs.length <= 10^4
 * 0 <= strs[i].length <= 100
 * strs[i] consists of lowercase English letters.
 * 
 * 
 */

// method: 
//      iterate through, use the sorted version of each string as the key in a map
//      

// @lc code=start
function groupAnagrams(strs: string[]): string[][] {
    // 26 primes, one for each letter of the alphabet
    const primes: number[] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101];

    function convertStringToPrime(str: string) {
        let p: number = primes[str.charCodeAt(0) - 97]

        for (let i = 1; i < str.length; i++) {
            p *= primes[str[i].charCodeAt(0) - 97]
        }
        return p
    }

    const map = new Map<number, string[]>();
    for (let str of strs) {
        const prime = convertStringToPrime(str)
        
        if (map.has(prime)) {
            map.get(prime)?.push(str)
        } else {
            map.set(prime, [str])
        }
    }

    return [...map.values()]

};
// function groupAnagrams(strs: string[]): string[][] {
//     let map = new Map<string, string[]>();
//     strs.forEach(str => {
//         const key = str.split('').sort().join('');
//         map.set(key, [...(map.get(key) ?? []), str]);
//     })
//     return [...map.values()];
// };
// function groupAnagrams(strs: string[]): string[][] {
//     const anagrams = {}
//     strs.forEach((val) => {
//         const key = val.split('').sort().join('');
//         if (anagrams[key] === undefined) anagrams[key] = [];
//         anagrams[key].push(val)
//     })
//     return Object.values(anagrams)
// };
// @lc code=end


// const primes: number[] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101];

// function convertStringToPrimeValue(s: string): number {
//     let total: number = 1;
//     for (let i = 0; i < s.length; i++) {
//         const c = s[i];
//         const primeNumber = primes[c.charCodeAt(0) - 97];
//         total *= primeNumber;
//     }
//     return total;
// }

// function groupAnagrams(strs: string[]): string[][] {
//     const groupedAnagrams: string[][] = [];
//     const groupAnagramMap: Map<number, number> = new Map();
//     for (let i = 0; i < strs.length; i++) {
//         const s = strs[i];
//         const primeValue: number = convertStringToPrimeValue(s);
//         if (groupAnagramMap.has(primeValue)) {
//             groupedAnagrams[groupAnagramMap.get(primeValue)].push(s);
//         } else {
//             groupAnagramMap.set(primeValue, groupedAnagrams.length);
//             groupedAnagrams.push([s]);
//         }
//     }
//     return groupedAnagrams;
// };