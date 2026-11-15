class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)
        start = 0
        end = n-1

        while start < end:

            char_start = s[start]
            char_end = s[end]

            if not char_start.isalnum():
                start += 1
                continue
            if not char_end.isalnum():
                end -= 1
                continue

            if char_start.lower() != char_end.lower():
                return False
            start += 1
            end -= 1

        return True

        