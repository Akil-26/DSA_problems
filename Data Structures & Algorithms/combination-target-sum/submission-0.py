class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def find(i,curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or sum(curr) > target:
                return
            curr.append(nums[i])
            find(i,curr)
            curr.pop()
            find(i+1,curr)
            return
        find(0,[])
        return res