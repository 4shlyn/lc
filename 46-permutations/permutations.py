class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = set(nums)
        def backtrack(path):
            if len(path)==len(nums):
                perms.append(path.copy(),)
                return
            choices = n-set(path)
            for c in choices:
                path.append(c)
                backtrack(path)
                path.pop()
        
        perms = []
        backtrack([])
        return perms