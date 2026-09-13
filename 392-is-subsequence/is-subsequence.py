class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        e = 0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if t[i] == s[e]:
                e+=1
                if e == len(s):
                    return True
        return False
            
        