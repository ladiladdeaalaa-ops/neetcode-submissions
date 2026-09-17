class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # groups={}
        temp=int(1)
        emptlist=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             temp+=1
        #     if nums[i] in groups:
        #         continue
              
        #     else:
        #         groups[nums[i]]=temp
        #     temp=1
        groups = {}

        for num in nums:

             if num in groups:
                groups[num] += 1
             else:
                groups[num] = 1
        sorteddict=dict(sorted(groups.items(),key=lambda item: item[1],reverse=True))
        for i in range(k):
           keyy= list(sorteddict)[i]
           emptlist.append(keyy)
    
        return emptlist

        