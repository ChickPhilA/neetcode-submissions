class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # our indices
        left = 0
        right = len(nums)-1
        middle = len(nums) // 2

        while left <= right:
            # three base cases

            # case 1: if the target already equals the
            # value at the middle index
            if nums[middle] == target:
                return middle

            # case 2: if target is greater than the middle,
            # change the left index to middle + 1.
            elif nums[middle] < target:
                left = middle + 1
                middle = (left + right) // 2

            # case 3: if the target is less than the middle value,
            # change the right index to middle - 1
            else:
                right = middle - 1
                middle = right // 2

        return -1 # target not found
