'''
26.删除排序数组中的重复项

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。

'''

def removeDuplicates(nums: List[int]) -> int:
        #排序数组 双指针
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                while count <= 2:
                    count += 1
                del nums[i - 1]
            count = 0
        return len(nums) 
            
#通过	92 ms	14.9 MB	python3


'''
80. 删除排序数组中的重复项 II
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
'''
def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2:
            return size
        # counter 表示下一个要覆盖的索引
        counter = 2 #count为1号指针
        # 索引为 0 和 1 的数一定会被保留，因此遍历从索引 2 开始
        for i in range(2, size): #i为2号指针
            if nums[i] != nums[counter - 2]:
                nums[counter] = nums[i]
                counter += 1
        return counter #counter不等于最后的list长度，counter等于遍历下去所有只含两个count的数字
#通过	68 ms	13.1 MB	python3


'''
27. 移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
'''
def removeElement(self, nums, val: int) -> int:
        
        # #倒着循环就不会产生错误 正循环会出现index 有问题
        # n = len(nums)
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == val:                
        #         count+=1
        #         nums.append(nums.pop(i))
        #     if i >0:
        #         i -=1
        # #del nums[n-count+1:n]
        # return len(nums)
        
#解法1        
#         for i in range(len(nums)-1,-1,-1):
#             if nums[i]==val:
#                 nums.pop(i)
#         return len(nums)

#解法2
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n  -= 1
            else:
                i += 1
        return n
#通过	56 ms	13.3 MB	python3


'''
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.append(nums.pop(i))
#通过	68 ms	13.1 MB	python3
