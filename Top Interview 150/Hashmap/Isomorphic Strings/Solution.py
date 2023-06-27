class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_map = {}
        for i in range(0, len(s)):
            if s[i] not in s_map:
                if t[i] not in s_map.values():
                    s_map[s[i]] = t[i]
                else:
                    return False
            elif s_map[s[i]] != t[i]:
                return False

        return True
