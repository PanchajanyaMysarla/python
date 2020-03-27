class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def f(log):
            idx,others = log.split(' ',1)
            print(idx,others)
            return (0,others,idx) if others[0].isalpha() else (1,)
        return sorted(logs,key=f)
        