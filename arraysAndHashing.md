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

#### Cpp
```cpp
#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seenSet;
        for (int i = 0; i < nums.size(); ++i){
            // cout << nums[i] << " " ;
            if (seenSet.count(nums[i])){
                return true;
            }
            seenSet.insert(nums[i]);
        }
        return false;
    }

};
int main(){
    Solution sol;
    vector<int> nums = {1,2,3,1};
    bool res = sol.containsDuplicate(nums);
    cout << (res ? "true" : "false") << endl ;
    return 0;

}

```
#### py3
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
#### Cpp
```cpp
#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) return false;
        vector<int> f(26,0);

        for (char c: s){
            f[c - 'a']++;
        }

        for (char c : t){
            f[c - 'a']--;
        }

        for (int e : f){
            if (e != 0) return false;
        }

        return true;
    }

};

int main()
{
    Solution sol;
    string s, t;
    cin >> s >> t ;
    bool res = sol.isAnagram(s,t);
    cout << (res? "true" : "false" ) << endl;
    return 0;

}

```
#### py3
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
#### Cpp
```cpp
#include<iostream>
#include<string>
#include<vector>
#include<unordered_map>
#include<sstream>
using namespace std;

class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap;

        for (int i = 0; i < nums.size(); ++i){
            int d = target - nums[i];

            // If d exists, it returns an iterator to the element.
            // If d does not exist, it returns hashMap.end().
            if (hashMap.find(d) != hashMap.end()) return {hashMap[d],i};
            hashMap[nums[i]] = i;
        }

        return {0,0};
    }
};


int main()
{
    Solution sol;

    int x, t;


    vector<int> nums;

    string ln;

    getline(cin, ln);

    stringstream ss(ln);

    for (int i = 0; ss >> x; ++i) nums.push_back(x);

    cin >> t;

    vector<int> res = sol.twoSum(nums, t);

    for (int e: res) cout << e << " " ;
    cout << endl;
    return 0;
}

```
#### py3
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

## 49. Group Anagrams  

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.  

### Example 1:  
**Input:**  
`strs = ["eat","tea","tan","ate","nat","bat"]`  

**Output:**  
`[["bat"],["nat","tan"],["ate","eat","tea"]]`  

**Explanation:**  
- There is no string in `strs` that can be rearranged to form `"bat"`.  
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.  
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.  


### Example 2:  
**Input:**  
`strs = [""]`  

**Output:**  
`[[""]]`  


### Example 3:  
**Input:**  
`strs = ["a"]`  

**Output:**  
`[["a"]]`  


### Constraints:  
- `1 <= strs.length <= 10^4`  
- `0 <= strs[i].length <= 100`  
- `strs[i]` consists of lowercase English letters.  

###Code
#### Cpp
```cpp
#include<iostream>
#include<vector>
#include<unordered_map>
#include<string>
#include<sstream>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;

        for (string w: strs){
            vector<int> f(26,0);
            for (char c: w) f[c - 'a']++;
            string key = "";
            // in one space for a string that makes # + 1 -> 1# or
            // # + 0 -> 0# string concatenation buddy
            for (int i = 0; i < 26; ++i) key += string(1,'#') + to_string(f[i]);

            hashMap[key].push_back(w);
        }
            vector<vector<string>> res;
            for (auto &kv: hashMap) res.push_back(kv.second);
            return res;
    }
};

int main()
{
    Solution sol;

    vector<string> strs;

    string ln;

    string x;

    getline(cin, ln);

    stringstream ss(ln);

    for(; ss >> x; ) strs.push_back(x);

    // for (string w: strs) cout << w << " ";
    // cout << endl;

    vector<vector<string>> res = sol.groupAnagrams(strs);

    for (auto kv: res) for (auto v:kv) cout << v << " ";
    cout << endl;

    return 0;
}

```
___
