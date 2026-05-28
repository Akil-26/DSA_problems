class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in mapp:
                return [mapp[dif],i]
            mapp[nums[i]] = i