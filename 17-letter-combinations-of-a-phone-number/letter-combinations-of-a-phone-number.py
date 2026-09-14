class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

            
        def backtrack(path, index):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return #backtrack

            possible_letters = m[digits[index]]
            for l in possible_letters:
                path.append(l) #add cur letter 
                backtrack(path, index+1) #next dig
                path.pop()#remove letter b4 moving to next
        
        combinations = []
        backtrack([],0)
        return combinations