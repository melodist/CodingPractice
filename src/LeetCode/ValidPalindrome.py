"""
Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
str.isalnum() : Return True if the string consists of alphanumeric characters.
str.casefold() : returns a string where all the characters are lower case.
filter(function, iterable) : Construct an iterator from those elements of iterable for which function returns true. 
iterable may be either a sequence, a container which supports iteration, or an iterator.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:        

        stripped = ''.join(filter(str.isalnum, s)).casefold()
        
        if stripped == stripped[::-1]:
            return True
        
        return False
