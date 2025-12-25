class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * (2*n)

        for i, a in enumerate(nums):

            ans[i] = a
            ans[i+n] = a 

        return ans