'''
Problem 3:

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.


Input: s = "eceba", k = 2

Output: 3

The substring is "ece" with length 3. 

Input: s = "aa", k = 1

Output: 2

The substring is "aa" with length 2. 
'''


def longestSubstring(s: str, k: int) -> int:
    if len(s) < k:
        return len(s)
    start = 0
    end = 0
    maxSubString = 0
    dict = {}

    while(end < len(s)):
        if s[end] in dict:
            dict[s[end]] += 1
        else:
            dict[s[end]] = 1

        # if dictionary has more than two values, we know the substring not valid
        while(len(dict) > k):
            dict[s[start]] -= 1
            if dict[s[start]] == 0:
                del dict[s[start]]
            start += 1
        if end - start + 1 > maxSubString:
            maxSubString = end-start + 1
        end += 1

    return maxSubString


print(longestSubstring("eceba", 2))
print(longestSubstring("aa", 1))
