class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        MAX = 2**32 -1
        n = len(nums)

        count_of_zeros = 0
        non_zero_product = 1
        for i in range(n):
            if nums[i] == 0:
                count_of_zeros += 1
            else:
                non_zero_product *= nums[i]

        
        if count_of_zeros > 1:
            return [0]*n

        products = []

        for i in range(n):
            if nums[i] == 0:
                product = non_zero_product
            elif count_of_zeros == 1 :
                product = 0
            else:
                product = non_zero_product//nums[i]

            products.append(product)

        return products
        

