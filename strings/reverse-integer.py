class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            x = int('-'+str(abs(x))[::-1])
        else:
            x = int(str(x)[::-1])
        if(x > -2147483648 and x < 2147483647):
            return x
        else:
            return 0