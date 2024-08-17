# problem 1
# ************************
"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
def reverseString(s):
    s = "".join(s)
    s = s[::-1]
    s = list(s)
    print(s)
# reverseString( ["H","a","n","n","a","h"])
def reverseString2(s):
    n = len(s)
    p1 = 0
    p2 = n -1
    
    while p1 < p2 :
        s[p1],s[p2] = s[p2],s[p1]
        p1 += 1
        p2 -= 1
    print(s)
# print(reverseString2(["H","a","n","n","a","h"]))
# problem 2
"""
1768. Merge Strings Alternately
Easy

3904

98

Add to List

Share
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
def mergeAlternately(word1,word2):
    n1 = len(word1)
    n2 = len(word2)
    mergedString = ""
    for i in range(min(n1,n2)):
        mergedString += word1[i]
        mergedString += word2[i]
    if(n2 > n1):
            mergedString += word2[n1:]
    elif n1 > n2:
            mergedString += word1[n2:]
    return mergedString
# print(mergeAlternately(word1 = "abc", word2 = "pqrzx"))