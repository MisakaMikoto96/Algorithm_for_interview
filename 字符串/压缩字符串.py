
‘’‘
示例 2：

输入：
["a"]

输出：
返回1，输入数组的前1个字符应该是：["a"]

说明：
没有任何字符串被替代。
示例 3：

输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。

’‘’

class Solution:
    def compress(self, chars: List[str]) -> int:
        # s = list(set(sorted(chars)))
        # ss = []
        # for i in s:
        #     num = chars.count(i)
        #     if num ==1:
        #         ss.append()
        #     if num > 1:
        #         ss += str(num)
        # return list(ss)
        
        
        
   def compress2(self, chars: List[str]) -> int:     
        end,count = 0,1
        for i in range(1,len(chars)+1):
            if i < len(chars) and chars[i-1]==chars[i]: #如果这个字母跟前一个相同
                count+=1 #记录这个字母的数目
            else:
                chars[end] = chars[i-1] #如果不同的话，用chars[i-1]这个字符把chars[end]替换掉 
                end +=1                 #end 往后移一格
                if count >1:            #如果count>1
                    for x in str(count):  
                        chars[end] = x  #将字母的数量写上，替换掉之前的
                        end+=1          #指针往后跳一格，为下一个字母的位置
                count =1                #初始化下一个字母的count！！！
        return end
        
 #通过	116 ms	12.9 MB	python3
