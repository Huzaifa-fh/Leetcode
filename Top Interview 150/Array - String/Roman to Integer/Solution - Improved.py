class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        size = len(s)

        for i in range(size):
            if i != size - 1 and roman_numerals[s[i + 1]] > roman_numerals[s[i]]:
                result -= roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]

        return result
