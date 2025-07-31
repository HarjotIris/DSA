from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ...
        '''
        map = {}

        for str in strs:
            sum = 0
            for char in str:
                sum += ord(char)

            if sum in map:
                map[sum].append(str)

            else:
                map[sum] = [str]

        result = []
        for key, value in map.items():
            result.append(value)

        return result
        '''
        '''
        anagram_map = {}
        for word in strs:
            key = tuple(sorted(word))

            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = word
        return list(anagram_map.values())
        '''

        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            anagram_map[key].append(word)

        return list(anagram_map.values())

sol = Solution()
print(sol.groupAnagrams(["a"]))