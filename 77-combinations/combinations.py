class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(path, index):
            if len(path) == k:
                combinations.append(path.copy())
                return
            for i in range(index,n+1):
                path.append(i)
                backtrack(path, i+1)
                path.pop()
        combinations = []
        backtrack([],1)
        return combinations
        