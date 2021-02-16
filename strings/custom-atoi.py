class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if(len(s) == 0):
            return 0
        string = ''
        sign = ''
        #create the sign
        if(s[0] == '+' or s[0] == '-'):
            if(s[0] == '-'):
                sign = s[0]
        #create the number
        for i in range(1 if s[0] == '+' or s[0] == '-' else 0,len(s)):
            if s[i].isdigit():
                string += s[i]
            else: 
                break
        #remove leading 0's
        string = re.sub(r'^0+','', string)
        string = sign + string
        #check if valid string
        if(len(string) == 1 or len(string) == 0) and not string.isdigit():
            return 0
        if int(string) > 2**31 - 1:
            return 2**31 - 1
        elif int(string) < -2**31:
            return -2**31
        else:
            return string
        return 0