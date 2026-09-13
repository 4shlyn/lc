class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            e = target-numbers[i]
            if numbers[j] > e:
                j-=1
            elif numbers[j] < e:
                i+=1
            elif numbers[j] == e:
                return [i+1,j+1]
        
        