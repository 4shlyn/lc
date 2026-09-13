class Solution:
    def maxArea(self, height: List[int]) -> int:
        mw = 0
        i=0
        j=len(height)-1
        while i < j:
            cw = min(height[i],height[j]) * (j-i)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            if cw > mw:
                mw = cw
            print(cw,mw)
        return mw