class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()

        if len(s_list) != len(pattern):
            return False

        s_map = {}
        for i in range(0, len(pattern)):
            if pattern[i] not in s_map:
                if s_list[i] not in s_map.values():
                    s_map[pattern[i]] = s_list[i]
                else:
                    return False
            elif s_map[pattern[i]] != s_list[i]:
                return False

        return True
