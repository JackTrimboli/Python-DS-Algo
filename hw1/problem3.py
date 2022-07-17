'''
Problem 3:

Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:

Input: s = "eceba"

Output: 3

Explanation: The substring is "ece" which its length is 3.

 

Input: s = "ccaabbb"

Output: 5

Explanation: The substring is "aabbb" which its length is 5.

Notes:
- use sliding window 


'''


def longestSubstring(s):
    if len(s) < 3:
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
        while(len(dict) > 2):
            dict[s[start]] -= 1
            if dict[s[start]] == 0:
                del dict[s[start]]
            start += 1
        if end - start + 1 > maxSubString:
            maxSubString = end-start + 1
        end += 1

    return maxSubString


print(longestSubstring("eceba"))
print(longestSubstring("ccaabbb"))
