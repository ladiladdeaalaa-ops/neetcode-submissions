class Solution:

    def encode(self, strs: List[str]) -> str:
       df=[]
       if(len(strs)>0):
        s="9#@".join(strs)
        return s
       elif(strs==[]):
        return "true" 

    def decode(self, s: str) -> List[str]:
        dd=[]
        ff=[""]
        if(s==""):
            return ff
        elif(s=="true"):
            return []
        else:

            output=s.split("9#@")
            return output

