class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}','[':']'}
        for i in range(len(s)):
            if s[i] in pairs:
                stack.insert(0,s[i])
            else:
                if stack:
                    if pairs[stack.pop(0)] != s[i]:
                        return False
                else:
                    return False

        if stack:
            return False
        return True          


                
            

        