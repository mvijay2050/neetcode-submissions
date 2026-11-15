class Solution:
    def isPalindrome(self, s: str) -> bool:


        def isAlphaNum(ch):

            if ( ord('A') <= ord(ch) <= ord('Z') ) or (
                ord('a') <= ord(ch) <= ord('z') ) or (
                ord('0') <= ord(ch) <= ord('9')
            ) : 
                return True
            else:
                return False




        n = len(s)
        start = 0
        end = n-1

        while start < end:

            char_start = s[start]
            char_end = s[end]

            if not isAlphaNum(char_start):
                start += 1
                continue
            if not isAlphaNum(char_end):
                end -= 1
                continue

            if char_start.lower() != char_end.lower():
                return False
            start += 1
            end -= 1

        return True




        