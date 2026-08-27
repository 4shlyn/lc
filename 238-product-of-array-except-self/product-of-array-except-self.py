class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        suffix = [1]
        n = len(nums) -1
        for i in range(n):
            prefix.append(nums[i]*prefix[i])
            suffix.append(nums[n-i]*suffix[i])
        e=[]
        for i in range(n+1):
            e.append(prefix[i]*suffix[n-i])
        return e