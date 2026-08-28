class Solution:
    def intToRoman(self, num: int) -> str:
        r = {0:'',1:'I', 5:'V', 10:'X', 50:'L', 100:'C',500:'D', 1000:'M',4:'VI',9:'XI',40:'LX',90:'CX',400:'DC',900:'MC'}
        a = ""
        #go back
        n = len(str(num))
        for i in range(n):
            cur = num%((10**i)*10)
            temp = int(str(num)[n-1-i])
            if temp !=0:
                base = int((cur/temp))
            f =""
            if temp > 5 and temp < 9:
                # cur = 700
                # i = 2
                # temp = 7
                f = r[base*5]
                num -= base*5
                temp -=5
                cur -= base*5
            if temp < 4 and temp > 0:
                a+=r[base]*temp # 100
                a+=f
                num -= cur
                continue

            a += r[cur]
            num -= cur
        return a[::-1]

        