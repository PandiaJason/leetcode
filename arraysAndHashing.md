# Array and Hashing


## 217. Contains Duplicate


---

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
