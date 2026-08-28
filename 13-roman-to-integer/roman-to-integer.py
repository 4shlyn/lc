class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        exc = {'IV':-1, 'IX':-1,'XL':-10,'XC':-10,"CD":-100,"CM":-100}
        a=0
        for i in range(len(s)):
            if s[i] in ('I','X','C') and i < len(s)-1:
                if s[i]+s[i+1] in (exc):
                    a+=exc[s[i]+s[i+1]]
                    print(s[i]+s[i+1])
                    continue

            a+=romans[s[i]]
        return a

        