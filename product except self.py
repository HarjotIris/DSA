class Solution: # optimal solution
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]    
        return res    
sol = Solution()
print(sol.productExceptSelf([-1,0,1,2,3]))



'''
class Solution: # brute force with hashmaps
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        helper = {index: value for index, value in enumerate(nums)}
        
        for i in range (len(nums)):
            mul = 1
            for j in range (len(nums)):
                if j == i:
                    continue
                else:
                    mul *= helper[j]
            result.append(mul)
            
        return result
        

sol = Solution()
print(sol.productExceptSelf([-1,0,1,2,3]))
'''