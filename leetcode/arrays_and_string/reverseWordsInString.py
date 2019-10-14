"""
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
"""

s1 = "the sky is blue"
s2= "a good   example"
s3="Let's take LeetCode contest"



def reverseWords(s):
    return ' '.join(s.split()[::-1])

#print(reverseWords(s2))


def revWords2(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return ' '.join(l)
    
print(revWords2(s3))