class Solution:
    def reverseWords(self, s: str) -> str:
        e = s.split(' ')
        e = [a for a in e if a != ""]
        return " ".join(e[::-1]).strip()
        