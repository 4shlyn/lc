class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(path, pSum, start):
            if pSum == target:
                combinations.append(path.copy())
                return
            elif pSum>target:
                return
            
            for c in range(start,len(candidates)):
                path.append(candidates[c])
                pSum+=candidates[c]
                backtrack(path,pSum,c)
                pSum-=candidates[c]
                path.pop()
                
            
        combinations = []
        backtrack([],0,0)
        return combinations