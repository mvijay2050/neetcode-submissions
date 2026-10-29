class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        # Brute force 
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]

        x = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in x:
                return [x[diff], i]
            else:
                x[nums[i]] = i