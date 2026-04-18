class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = 0
        for num in nums:
            curr = max(num,num+prev)
            res = max(res,curr)
            prev = curr
        return res