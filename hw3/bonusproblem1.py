'''
1) Edit Distance Problem


Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
Example 1:

Input: s = "ab", t = "acb"

Output: true

Explanation: We can insert 'c' into s to get t.

Example 2:

Input: s = "", t = ""

Output: false

Explanation: We cannot get t from s by only one step.

Example 3:

Input: s = "", t = "A"

Output: true
'''
