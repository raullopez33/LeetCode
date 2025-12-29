class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1 
        for i in range((n+1)//2):
            tmp = s[i]
            s[i]=s[n-i]
            s[n-i] = tmp 
        