class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        maxi = 0
        for k in freq_dict:
            if freq_dict[k] > maxi:
                maxi = freq_dict[k]
                maj = k

        return maj

sol = Solution()
print(sol.majorityElement([3,2,3,2,1,1,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))
'''
count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
this solution doesn't work tho for the case of [3,2,3,2,1,1,3] because 
three is the majority element here but it doesn't show that.
'''