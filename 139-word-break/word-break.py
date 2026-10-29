

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = [None] * (len(s) + 1)

        def solve(s):
            if len(s) == 0:
                return True

            if memo[len(s)] is not None:
                return memo[len(s)]

            for word in wordDict:
                w = len(word)

                if len(s) >= w and s[len(s)-w:] == word:
                    if solve(s[:len(s)-w]):
                        memo[len(s)] = True
                        return True

            memo[len(s)] = False
            return False

        return solve(s)
