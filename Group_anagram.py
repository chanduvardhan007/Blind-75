class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic=defaultdict(list)
        # for i in strs:
        #     count=[0]*26
        #     for s in i:
        #         count[ord(s)-ord('a')]+=1
        #     dic[tuple(count)].append(i)
        # return dic.values()

        # Method 2
        dic={}
        for i in strs:
            j=''.join(sorted(i))
            if j not in dic.keys():
                dic[j]=[]
                dic[j].append(i)
            else:
                dic[j].append(i)
        return dic.values()
