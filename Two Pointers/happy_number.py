class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1 or n == 10:
            return True
        seen = {}
        curr_sum = 0
        num = [int(nu) for nu in str(n)]
        
        while curr_sum not in seen:
            left, right = 0, len(num) - 1
            while left < right:
                curr_sum = pow(num[left], 2) + pow(num[right], 2)
                left += 1
                right -= 1
            seen[curr_sum] = 1
            num = [int(nu) for nu in str(curr_sum)]
            
        
        if curr_sum == 1:
            return True
        return False