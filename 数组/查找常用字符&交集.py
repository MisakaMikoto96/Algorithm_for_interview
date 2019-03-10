'''
1002. 查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

 

示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]
'''

def commonChars(A: List[str]) -> List[str]:
        result = []
        for chara in A[0]:
            if all(chara in j for j in A[1:]):
                result.append(chara)
            for x in range(1,len(A)): #从A[1]开始遍历之后的
                if chara in A[x]: #如果这个字符在A[x]里
                    index = A[x].find(chara) #找到这个字符的位置
                    A[x] = A[x][:index]+A[x][index+1:] #把字符里这个元素给删掉,继续查找
        return result
#通过	112 ms	13.3 MB	python3


'''
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

'''
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        intersection = set(nums1)&set(nums2) #&为两个dict的交集
        for i in intersection: #可以对set里面的元素进行遍历
            num = [i] * min(nums1.count(i),nums2.count(i)) #找到两个list里 这个数的最小个数
            res += num
        return res
#通过	136 ms	13.3 MB	python3


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        #Counter类：为hashable对象计数，是字典的子类
        #elements()元素被重复了多少次，在该迭代器中就包含多少个该元素。元素排列无确定顺序，个数小于1的元素不被包含。
        
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements()) #list一个dict后得到的是dict的keys
#通过	88 ms	13.4 MB	python3

#元素唯一的交集
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set(nums1)&set(nums2))
    
        num_dict = {}
        res = []
        for i in nums1:
            if i in num_dict:
                num_dict[i]+=1
            else:
                num_dict[i]=0
        for i in nums2:
            if i in num_dict:
                res.append(i)
        return list(set(res))
