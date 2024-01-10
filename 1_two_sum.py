class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range (len(nums)-1-i):
                if(nums[i] + nums[j+1+i] == target):
                    first = i
                    second = j+1+i
                    
        return first, second