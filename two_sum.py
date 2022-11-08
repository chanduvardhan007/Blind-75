class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,v in enumerate(nums):
            n=target-nums[i]
            if n in a:
                return [i,a[n]]
            a[v]=i
