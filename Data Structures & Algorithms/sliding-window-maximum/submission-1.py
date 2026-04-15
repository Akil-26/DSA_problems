class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Deque = []
        res = []
        left = right = 0
        while right < len(nums):
            while Deque and nums[Deque[-1]] < nums[right]:
                Deque.pop()
            Deque.append(right)

            if left>Deque[0]:
                Deque.pop(0)
            if (right + 1) >= k:
                res.append(nums[Deque[0]])
                left += 1
            right += 1
        return res