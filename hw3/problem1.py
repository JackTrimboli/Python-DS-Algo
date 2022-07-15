'''
Problem 1:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
'''


def isAnagram(s, t):
    return sorted(s) == sorted(t)


def isAnagram2(s, t):
    d1, d2 = {}, {}
    for item in s:
        d1[item] = d1.get(item, 0) + 1
    for item in t:
        d2[item] = d2.get(item, 0) + 1
    return d1 == d2


print(isAnagram("rat", "car"))
print(isAnagram("anagram", "nagaram"))

print(isAnagram2("rat", "car"))
print(isAnagram2("anagram", "nagaram"))
