class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Method 1
        # if(len(nums) != len(set(nums))):
        #     return True
        # l=[0]*(len(nums)+1)

        #Method 2
        dic={}
        for i in range(len(nums)):
           if nums[i] in dic:
               return True
           dic[nums[i]]=nums[i]
        return False
        
