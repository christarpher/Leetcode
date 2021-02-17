class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i = 0
        string = ""
        shortest = min(strs, key=len)
        while i < len(shortest):
            for item in strs:
                if item[i] != shortest[i]:
                    return string
            else:
                string += item[i]
            i += 1
        return string