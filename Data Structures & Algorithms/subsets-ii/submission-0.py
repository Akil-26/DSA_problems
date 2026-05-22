class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def fun(i,sub):
            res.append(sub[::])
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                sub.append(nums[j])
                fun(j+1,sub)
                sub.pop()
        fun(0,[])
        return res