class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        box = set()

        for ind in nums:
            if ind in box:
                return True
            box.add(ind)
        return False