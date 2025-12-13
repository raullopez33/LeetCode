# Intuition
'''
<!-- Describe your first thoughts on how to solve this problem. -->
We have to iterate through each digit to know if its palindrome
and start from both ends and work from there 

Two pointer solution that initially came to mind 

'''

# Approach
#<!-- Describe your approach to solving the problem. -->
'''
First turn integer to string and then instantiate the left most pointer and right most pointer
to go start l,r = 0, len(int->str) 

Do a while loop that stops when l == r or l>r : l < r must suffice for while loop to run

'''
'''
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

"""
This is an O(n/2) --> O(n) since big O ignores constants 
"""

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(n)
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = str(x)
        l,r = 0 , len(new)-1

        while(l<r):

            if new[l] != new[r]:
                return False
    
            l += 1 
            r -= 1 
        return True



            
            

            


        