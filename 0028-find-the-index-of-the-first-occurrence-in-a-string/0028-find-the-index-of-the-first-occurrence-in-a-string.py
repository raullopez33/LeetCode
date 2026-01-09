class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            wor = haystack[i:i+len(needle)]
            if wor == needle:
                return i
            
        return -1