class Solution: 
    def majorityElement(self, nums: list[int]) -> list[int]:
        threshold = len(nums)/3

        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        res = []

        for k in freq_dict:
            if freq_dict[k] > threshold:
                res.append(k)

        return res
    
sol = Solution()
print(sol.majorityElement([3, 2, 3]))
print(sol.majorityElement([1]))
print(sol.majorityElement([1, 2]))