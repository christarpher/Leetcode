class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for item in digits:
            string += str(item)
        string = str(int(string) + 1)
        digits.clear()
        for integer in string:
            digits.append(int(integer))
        return digits