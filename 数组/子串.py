'''
78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            for j in range(len(ans)): 
                ans.append(ans[j]+[nums[i]])
        return ans
        
'''***************************************
len(ans)=1
i = 0 j = 0 --->[[],[1]]

len(ans)=2
i = 1 j = 0 --->[[],[1],[2]]
      j = 1 --->[[],[1],[2],[1,2]]
      
len(ans)=4
i = 2 j = 0 --->[[],[1],[2],[1,2],[3]]
      j = 1 --->[[],[1],[2],[1,2],[3],[1,3]]
      j = 2 --->[[],[1],[2],[1,2],[3],[1,3],[2,3]]
      j = 3 --->[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
      
第n位可以生成2**n个含n的子集
[]
[1]
[2],[1,2]
[3],[1,3],[2,3],[1,2,3]
[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]
'''***************************************




'''
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [nums]
        t = [res[0]] #len(t)越来越小
        while t:
            x = []
            for item in t:
                for i in range(len(item)):
                    if item[:i]+item[i+1:] not in x: #剔除掉除重复
                        x+= [item[:i]+item[i+1:]] #除i元素之外所有元素的排列组合 依次遍历 len越来越小
            res += x #收集所有的答案x
            t = x 
        return res

      #python中字符串的 maketrans(in,out),translate(trantabl,'something')挺有用的
      
