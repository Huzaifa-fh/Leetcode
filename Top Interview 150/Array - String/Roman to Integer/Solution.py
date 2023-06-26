class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        chars = list(s)
        result = 0
        result_list = []
        dum_list = []

        for i in range(len(chars)):
            current_numeral  = chars[i]
            next_numeral = chars[i + 1] if i + 1 < len(chars) else None

            if next_numeral is not None and self.roman_numerals[next_numeral] >= self.roman_numerals[current_numeral]:
                dum_list.append(current_numeral)
                new_string = "".join(dum_list) + next_numeral
            else:
                dum_list.append(current_numeral)
                result_list.append("".join(dum_list))
                dum_list = []

        for ele in result_list:
            curr = list(ele)

            if len(curr) == 1:
                result += self.roman_numerals[curr[0]]
            elif self.roman_numerals[curr[0]] < self.roman_numerals[curr[1]]:
                dum = self.roman_numerals[curr[1]] - self.roman_numerals[curr[0]]
                result += dum
            elif self.roman_numerals[curr[0]] == self.roman_numerals[curr[1]]:
                result += self.roman_numerals[curr[1]] + self.roman_numerals[curr[0]]

            for i in range(2, len(curr)):
                result += self.roman_numerals[curr[i]]

        return result
