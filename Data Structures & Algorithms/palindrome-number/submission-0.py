class Solution:
    def isPalindrome(self, x: int) -> bool:


        if x < 0:
            return False

        rev = 0
        org = x
        while x != 0:
            rev = rev*10 + x%10
            x = x//10

        if rev == org:
            return True
        
        return False

        