class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = [c.lower() for c in s if c.isalnum()]

        i = 0
        j = len(alphanumeric) - 1

        while i <= j:
            if alphanumeric[i] != alphanumeric[j]:
                return False
            i += 1
            j -= 1

        return True
