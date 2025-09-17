# Array and Hashing


## 217. Contains Duplicate


Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.


### Example 1:
**Input:**  
`nums = [1,2,3,1]`  

**Output:**  
`true`  

**Explanation:**  
The element `1` occurs at the indices `0` and `3`.


### Example 2:
**Input:**  
`nums = [1,2,3,4]`  

**Output:**  
`false`  

**Explanation:**  
All elements are distinct.


### Example 3:
**Input:**  
`nums = [1,1,1,3,3,4,3,2,4,2]`  

**Output:**  
`true`



### Constraints:
- `1 <= nums.length <= 10^5`  
- `-10^9 <= nums[i] <= 10^9`


### Code 
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
```
---

## 242. Valid Anagram


Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.


### Example 1:
**Input:**  
`s = "anagram", t = "nagaram"`  

**Output:**  
`true`


### Example 2:
**Input:**  
`s = "rat", t = "car"`  

**Output:**  
`false`



### Constraints:
- `1 <= s.length, t.length <= 5 * 10^4`  
- `s` and `t` consist of lowercase English letters.  


### Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = [0] * 26
        for c in s:
            f[ord(c) - ord('a')]+=1
        for c in t:
            f[ord(c) - ord('a')]-=1
        for i in f:
            if i != 0:
                return False
        return True
```
---

## 1. Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.  

You can return the answer in any order.


### Example 1:
**Input:**  
`nums = [2,7,11,15], target = 9`  

**Output:**  
`[0,1]`  

**Explanation:**  
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.


### Example 2:
**Input:**  
`nums = [3,2,4], target = 6`  

**Output:**  
`[1,2]`


### Example 3:
**Input:**  
`nums = [3,3], target = 6`  

**Output:**  
`[0,1]`


### Constraints:
- `2 <= nums.length <= 10^4`  
- `-10^9 <= nums[i] <= 10^9`  
- `-10^9 <= target <= 10^9`  
- `Only one valid answer exists.`


### Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in hashMap:
                return [hashMap[d],i]
            hashMap[nums[i]] = i
        return [0,0]
```
---
