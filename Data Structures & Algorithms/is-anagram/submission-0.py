from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l1 = len(s)
        l2 = len(t)

        if l1 != l2 :
            return False

        seen = defaultdict(int)

        for i in range(l1):
            x1 = s[i]
            x2 = t[i]
            seen[x1] = seen[x1] + 1
            seen[x2] = seen[x2] - 1

        for values in seen.values():
            if values != 0:
                return False

        return True