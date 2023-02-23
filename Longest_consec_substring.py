class Solution:
    def Longest_consec_substring(s):
        length=0
        left,right=0,0
        max_len=0
        l=set()
        while(right<len(s)):
            if s[right] not in l:
                l.add(s[right])
                right+=1
                length+=1   
            elif s[right] in l:
                l.remove(s[left])
                left+=1
                length-=1
            max_len=max(max_len,length)
        return max_len
    print(Longest_consec_substring("abcabcbb"))