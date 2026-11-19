class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2

        while left != right:
            middle = (left + right) // 2
            # we know here from middle to right index, the array
            # is cleanly sorted. there, the min is on the left
            if nums[middle] < nums[right]:
                right = middle
                # or, the min is on the right, if the middle is bigger 
            # than the right index
            elif nums[middle] > nums[right]:
                left = middle + 1
            
        return nums[left] # can be left or right, since both pointers
        # will eventually meet at one point