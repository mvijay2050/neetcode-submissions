class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anaMap = {}

        for name in strs:
            chars = [0]*26
            for ch in name:
                asc = ord(ch) - ord('a')
                chars[asc] = chars[asc] + 1

            charTup = tuple(chars)
            anaMap[charTup] = anaMap.get(charTup, []) + [name]

        res = []
        for value in anaMap.values(): 
            res.append(value)

        return res