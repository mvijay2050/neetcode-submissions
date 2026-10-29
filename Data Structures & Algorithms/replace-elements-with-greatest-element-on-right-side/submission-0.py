class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        greatest  = -1

        n = len(arr)

        for i in range(n-1, -1, -1):
            current = arr[i]
            arr[i] = greatest
            greatest = max(greatest, current)


        return arr