class Solution: # Optimal Hash Map Solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # store data in value : index pairs
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return    
    
sol = Solution()
print(sol.twoSum([3,4,5,6], 7)) # [0,1]
print(sol.twoSum([4,5,6], 10))  # [0,2]
print(sol.twoSum([5, 5], 10))   # [0,1]

'''
class Solution: # Not optimal Hash Maps
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ...
        # we need target - value_1 = value_2
        prevMap = {} # store data in value : index pairs
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i

sol = Solution()
#print(sol.twoSum([3,4,5,6], 7)) 
#print(sol.twoSum([4,5,6], 10))
#print(sol.twoSum([5, 5], 10))
'''


'''
class Solution: #Brute Force
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
#print(sol.twoSum([3,4,5,6], 7)) 
#print(sol.twoSum([4,5,6], 10))
print(sol.twoSum([5, 5], 10))
'''
