class Solution: # Bucket Sort --> TC - O(n), Memory - O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for num, count in count.items():
            freq[count].append(num)

        result = []
        # go through "freq" in descending order cause we need "k" most frequent elements
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))
#print(sol.topKFrequent([7,7], 1))
        

'''
class Solution: # Sorting --> TC - O(nlogn), Memory - O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq_dict = {}
        result = []
        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i, 0)

        arr = []
        for num, freq in freq_dict.items():
            arr.append([freq, num])
        arr.sort()

        while len(result) < k:
            result.append(arr.pop()[1])
        return result

sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))
#print(sol.topKFrequent([7,7], 1))
'''