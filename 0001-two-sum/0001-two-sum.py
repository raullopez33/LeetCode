class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        h_m = num : indices
        
        loop through nums
        new_target = target - nums[i]

        if new_target in the h_m 
            return [i, h_m[new_target]]
        
        assume each input have exactly one solution then we can just keep that return value
        as is 
        '''

        h_m = {}

        for i in range(len(nums)):
            new_pos = target - nums[i]
            if new_pos in h_m:
                return [i, h_m[new_pos]]
            h_m[nums[i]] = i
        return []




            

            