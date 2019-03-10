'''
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
'''


#递归
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans_list=[]
        candidates.sort()
        for index,item in enumerate(candidates):
            if candidates[index] == target:
                ans_list.append([item])
            elif candidates[index]<target:
                tmp = self.combinationSum(candidates[index:],target-candidates[index]) #tmp返回[]
                for single_ans in tmp: #[[],[]]
                    single_ans.append(candidates[index]) 
                ans_list+=tmp
        return ans_list
#通过	108 ms	13.2 MB	python3


#深度优先搜索
def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(results,result,candidates,target,level):
            if target == 0:
                results.append(list(result))
                return
            elif target > 0:
                for i in range(level,len(candidates)):
                    result.append(candidates[i])
                    dfs(results,result,candidates,target-candidates[i],i)
                    result.pop()
                    
        results = []
        dfs(results,[],candidates,target,0)
        return results
                
