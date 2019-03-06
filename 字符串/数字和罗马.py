
'''数字转罗马'''
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            ['','M','MM','MMM'],#1000 2000 3000
            ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'], # 100-900
            ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'], # 10 - 90
            ['','I','II','III','IV','V','VI','VII','VIII','IX']  # 1  - 9
        ]
        
        digit=[1000,100,10,1]
        r = ''
        
        for index,value in enumerate(digit):
            r += roman[index][num/value]
            num = num % value #整除的余数    
        return r
        
        
        
'''罗马转数字'''
class Solution:
    def romanToInt(self, s:str) -> str:
        res = ''
        dict = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        for i in range(len(s)): #遍历每一个字符串
            if i < len(s-1) and dict[s[i]]<dict[s[s+1]]:
                res -= dict[s[i]]#碰到左边比右边小的，减去
            else:
                res += dict[s[i]]
        return res
        
        
        
