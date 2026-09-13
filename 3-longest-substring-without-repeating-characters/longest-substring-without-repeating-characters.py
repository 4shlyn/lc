class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        seen=set()
        i = 0
        j = 0
        if len(s)==0:
            return 0
        while i < len(s) and j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                if j-i > max:
                    max = j-i
                j+=1
                continue
            while s[i] != s[j]:
                seen.remove(s[i])
                i+=1
            if s[i]==s[j]:
                i+=1
            j+=1
        return max+1




        