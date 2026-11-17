class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:

        strs = [] 
        
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            name = s[j+1: j+1+length]
            i = j+1+length
            strs.append(name)

        return strs