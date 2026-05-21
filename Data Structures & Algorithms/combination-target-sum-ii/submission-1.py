class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(st,curr,tot):
            if tot == target:
                res.append(curr[:])
                return
            for i in range(st,len(candidates)):
                if i > st and candidates[i] == candidates[i-1]:
                    continue
                if tot + candidates[i] > target:
                    break
                curr.append(candidates[i])
                dfs(i+1,curr,tot+candidates[i])
                curr.pop()
        dfs(0,[],0)
        return res