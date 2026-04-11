class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dic = {}
        max_len = 0
        max_f = 0
        left = 0
        for right in range(len(s)):
            char_dic[s[right]] = char_dic.get(s[right],0)+1
            max_f = max(max_f,char_dic[s[right]])
            while (right-left+1) - max_f > k:
                char_dic[s[left]] -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len