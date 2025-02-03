class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []

        for i in range(n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        
        return res

sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(5))
print(sol.fizzBuzz(15))