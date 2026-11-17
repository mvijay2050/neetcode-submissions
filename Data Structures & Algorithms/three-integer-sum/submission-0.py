class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_sorted = sorted(nums)
        n = len(nums_sorted)

        three_sum = []

        for i in range(n):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue

            start = i+1
            end  = n-1

            while start < end:
                total = nums_sorted[i] +nums_sorted[start] + nums_sorted[end]

                if total == 0:
                    three_sum.append([nums_sorted[i], nums_sorted[start], nums_sorted[end]])
                    start = start +1
                    end = end -1
                    while start < end and nums_sorted[start] == nums_sorted[start-1]:
                        start = start+1
                elif total > 0:
                    end = end -1
                else:
                    start = start +1

        return three_sum
                    


        