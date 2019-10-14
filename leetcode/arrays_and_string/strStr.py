"""
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""

# haystack = 'hello'
# needle = 'll'

haystack = "aaaaa"
needle = "bba"

def strStr( haystack: str, needle: str) -> int:
    return haystack.find(needle)

print(strStr(haystack,needle))