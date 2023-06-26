class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rChar_map = {}
        mChar_map = {}

        for c in ransomNote:
            if c in rChar_map:
                rChar_map[c] += 1
            else:
                rChar_map[c] = 1

        for c in magazine:
            if c in mChar_map:
                mChar_map[c] += 1
            else:
                mChar_map[c] = 1

        if len(mChar_map) < len(rChar_map):
            return False

        for c in ransomNote:
            if c not in mChar_map:
                return False
            else:
                mChar_map[c] -= 1
            if mChar_map[c] == 0:
                del mChar_map[c]

        return True
