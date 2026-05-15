class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find(path):
            if len(nums) == len(path):
                res.append(path[:])
                return
            if len(path) > len(path):
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                find(path)
                path.pop()
        res = []
        find([])
        return res