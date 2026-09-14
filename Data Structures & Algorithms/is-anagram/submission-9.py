class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp=int(0)
        sorteds=''.join(sorted(s))
        sortedt=''.join(sorted(t))

        if sorteds==sortedt:
            return True
        else:
            return False
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i]==t[j]:
        #             temp+=1
        #             break
        # if temp==len(t) and len(t)==len(s):
        #     return True
        # else:
        #     return False
        