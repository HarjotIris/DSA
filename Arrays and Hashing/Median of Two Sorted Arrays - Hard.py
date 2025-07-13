class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2
        mid = total_len // 2
        merged_nums = []
        while i < len1 and j < len2 and len(merged_nums) <= mid:
            if nums1[i] <= nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            
            else:
                merged_nums.append(nums2[j])
                j += 1


        
        while i < len1 and len(merged_nums) <= mid:
            merged_nums.append(nums1[i])
            i += 1

        while j < len2 and len(merged_nums) <= mid:
            merged_nums.append(nums2[j])
            j += 1
        
        
        if total_len % 2 == 0 :
            return (merged_nums[mid - 1] + merged_nums[mid]) / 2
        else:
            return merged_nums[mid]

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))  
print(sol.findMedianSortedArrays([1, 2], [3, 4]))      
                