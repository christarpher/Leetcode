class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for element in range(len(s)):
            if s[element] not in table:
                table[s[element]] = 1
            else:
                table[s[element]] += 1
        for element in table:
            if(table[element]) == 1:
                 return s.find(element)
        return -1