#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        c = []
        for i in range(0,n):
            c.append(nums[i])
            c.append(nums[i+n])
        return c        
        
