class Solution: # using hash set, time complexity - O(n), memory complexity - O(n)
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in num_set:
            # check if it's a start of a sequence by checking if a left neighbor exists
            if (num - 1) not in num_set:
                length = 1 # length of the sequence thus far
                while (num + length) in num_set:
                    length += 1 
                result = max(result, length)
        return result
       
   
sol = Solution()
print(sol.longestConsecutive([2,20,4,10,3,4,5]))
        