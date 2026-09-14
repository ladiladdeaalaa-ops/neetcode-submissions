class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptlist=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    emptlist.extend([i,j])
                    # emptlist.append(j)

                    return emptlist
        