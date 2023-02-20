class Solution:
    def isPalindrome(s):
       #Method 1
        # s=''.join(filter(str.isalnum, s)).lower()
        # r=s[::-1]
        # if r == s:
        #     return True
        # return False

        #Method 2
        res=''
        for i in range(len(s)):
            if s[i].isalnum():
                res+=s[i].lower()
        reverse=res[::-1]
        return res==reverse
        
    print(isPalindrome("A man, a plan, a canal: panama"))