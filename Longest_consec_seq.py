
class Solution:
    def Longest_consec_seq(nums):
        s=set(nums)
        max_len=0
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                j=nums[i]
                while(j in s):
                    j+=1
                max_len=max(j-nums[i],max_len)
        return max_len
        
    print(Longest_consec_seq([100,4,200,1,3,2]))