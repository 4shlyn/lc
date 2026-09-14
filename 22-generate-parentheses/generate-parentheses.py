class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = ["(",")"]
        def backtrack(path,counts):
            if counts[0] == n and counts[1] == n:
                combinations.append("".join(path.copy()))
                return
            for c in range(2):
                if counts[c]==n:
                    continue
                if c==1 and counts[0] == counts[1]:
                    continue
                path.append((brackets[c]))
                counts[c]+=1
                backtrack(path,counts)
                path.pop()
                counts[c]-=1
        
        combinations=[]
        backtrack([],[0,0])

        return combinations