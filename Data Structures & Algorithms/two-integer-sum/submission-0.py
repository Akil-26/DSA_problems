class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            dic[n]=i
        for i, n in enumerate(nums):
            val = target - n
            if val in dic and dic[val] != i:
                return [i,dic[val]]