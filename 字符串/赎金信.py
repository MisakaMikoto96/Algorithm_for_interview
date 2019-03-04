‘’‘
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
’‘’



def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #done = []
        for i in range(len(ransomNote)):
            #if ransomNote[i] not in done: #如果ransom里的字符不在done里出现
                #并且如果ransom里这个字符的数目 小于等于 magazine里这个字符的数目 则跳转到done.append
                if ransomNote.count(ransomNote[i]) <= magazine.count(ransomNote[i]):
                    pass
                else: #不然就return False
                    return False
                #done.append(ransomNote) #跳转
        return True
        
#通过	360 ms	13.3 MB	python3



def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
    import re
    import re
    for char in ransomNote:
        #re.subn 替换删除函数，将magazine里的char替换，返回替换的次数
        ret_str, num = re.subn(char, '', magazine, count=1)  #count=1是为了不让在某一个字符没匹配的时候return false跳出
        magazine = ret_str
        if not num: return False
    return True
    
#通过	68 ms	13.5 MB	python3



# re.subn('a','bbb','aaaackdkwfaa',count=1) count=1即只匹配替换第一个
#   ——>('bbbaaackdkwfaa', 1)
