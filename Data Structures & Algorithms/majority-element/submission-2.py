class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        majority_element = nums[0]
        majority_element_count = 1
        for i in range(1, n):


            if majority_element_count ==0:
                majority_element_count = 1
                majority_element = nums[i]
            elif nums[i] == majority_element:
                majority_element_count += 1
            else:
                majority_element_count -= 1
                

        return majority_element