class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset=set()
        temp=int(0)

        for i in range(len(nums)):
            if nums[i] in myset:
                # return True
                temp+=1
            else:
                myset.add(nums[i])
        if temp>=int(1):
            return True
        else: 
            return False
            