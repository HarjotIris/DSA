class Solution:

    def encode(self, strs: list[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s       
        return enc 

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: length + j + 1])
            i = j + 1 + length
        return res
            

sol = Solution()
#r = sol.encode([])
#print(sol.decode(r)) 
s = sol.encode(["have", "a", "good", "day"])
print(sol.decode(s))

