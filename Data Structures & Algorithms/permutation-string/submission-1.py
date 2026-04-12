class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False

        s1Count,s2Count = [0] * 26,[0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            match += 1 if s1Count[i] == s2Count[i] else 0
        left = 0
        for right in range(len(s1),len(s2)):
            if match == 26: return True

            idx = ord(s2[right]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                match+=1
            elif s1Count[idx] + 1 == s2Count[idx]:
                match-=1
            
            idx = ord(s2[left]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                match += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                match -= 1
            left+=1
        return match == 26