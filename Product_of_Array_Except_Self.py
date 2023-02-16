
class Solution:
    def Product_array(nums):
        temp=[1]*len(nums)
        pre=1;post=1
        for i in range(len(nums)):
            temp[i]=pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            temp[i]*=post
            post*=nums[i]
        return temp
    Product_array([1,2,3,4])