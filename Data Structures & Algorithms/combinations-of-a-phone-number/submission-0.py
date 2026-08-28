class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(digits,i,curr):
            if i==len(digits):
                if curr!="":
                    res.append(curr)
                return 
            for com in comb[digits[i]]:
                backtrack(digits,i+1,curr+com)

        comb={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        backtrack(digits,0,"")
        return res
