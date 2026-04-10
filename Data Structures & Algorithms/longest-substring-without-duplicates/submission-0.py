class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_c = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_c = max(max_c,right-left+1)
        return max_c