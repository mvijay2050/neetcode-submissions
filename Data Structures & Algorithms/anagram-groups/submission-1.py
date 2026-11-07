class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anaMap = {}
        for name in strs:
            sortedName = "".join(sorted(name))
            anaMap[sortedName] = anaMap.get(sortedName, []) + [name]


        res = []
        for value in anaMap.values():
            res.append(value)

        return res