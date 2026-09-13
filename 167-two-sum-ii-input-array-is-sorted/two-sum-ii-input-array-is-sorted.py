class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            lo, hi = i + 1, n - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return [-1, -1]