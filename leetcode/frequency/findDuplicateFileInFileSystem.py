"""
609. Find Duplicate File in System
Medium

367

520

Add to List

Share
Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""

from collections import defaultdict
import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        d = collections.defaultdict(list)
        ans = []
        for p in paths:
            directory, files = p.split(' ',1)            
            file_n_contents= files.split()
            for i in file_n_contents:
                name,content = i.split('(',1)
                content = content.replace(')','')
                d[content].append(directory+'/'+ name)

        for item in d:
            if len(d[item]) >1:
                ans.extend([d[item]])
        return ans
           
                
        