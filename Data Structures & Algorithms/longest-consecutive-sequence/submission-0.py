class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        # [0,3,2,5,4,6,1,1]

    
        longest_seq = 0
        for num in nums:
            current_long = 0
            if (num-1) not in numSet:
                current_long = 0

                while (num+current_long) in numSet:
                    current_long += 1

                longest_seq = max(longest_seq, current_long)

        return longest_seq