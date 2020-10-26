"""
Author: Srinidhi
Did it run on LC: No - TLE
Time Complexity: O(n!) - Generating all the possible permutations of the given array of "n" numbers
Space Complexity: O(n) - The depth of recursion stack will go to n unique numbers at each branch
Logic:
Generate all the possible combinations and for each combination check the condition nums[i]%i and i%nums[i].
Increment the counter based on the condition being satisfied.

"""
class Solution:
    def countArrangement(self, N: int) -> int:
        self.count = 0
        nums = [i+1 for i in range(N)]
        self.permute(nums,0)
        return self.count
    
    def permute(self,nums,index):
        
        def swap(nums,x,y):
            nums[x],nums[y] = nums[y],nums[x]
            
        
        if index == len(nums)-1:
            for i in range(1,len(nums)):
                if (nums[i]%i!=0 or i%nums[i-1])!=0:
                    break
            
                if i == len(nums):
                    print(i)
                    self.count+=1
        
        for i in range(index,len(nums)):
            swap(nums,i,index)
            self.permute(nums,index+1)
            swap(nums,i,index)