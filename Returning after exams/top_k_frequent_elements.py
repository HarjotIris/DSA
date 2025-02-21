class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        max_freq = [key for key, _ in sorted(freq_dict.items(), key=lambda item : item[1], reverse=True)[:k]]
                     
        
        return max_freq

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([1], 1))
        