class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        backup_x = x
        reversed_x = 0

        while x > 0:
            remainder = x % 10
            x = x // 10
            reversed_x = (reversed_x * 10) + remainder

        if backup_x != reversed_x:
            return False

        return True
