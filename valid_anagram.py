class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1
        # dic1,dic2={},{}
        # for i in s:
        #     if i not in dic1.keys():
        #         dic1[i]=1
        #     else:
        #         dic1[i]+=1
        # for i in t:
        #    if i not in dic2.keys():
        #         dic2[i]=1
        #    else:
        #        dic2[i]+=1

        # return dic1==dic2

        # Method 2
        return Counter(s)==Counter(t)
        
