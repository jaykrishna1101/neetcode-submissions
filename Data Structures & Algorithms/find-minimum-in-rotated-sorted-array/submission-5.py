class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if left == right:
            return nums[left]
        m = nums[0]

        while right >= left:
            mid = (left + right) // 2

            m = min(nums[mid], m)
            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid - 1
            

        return m
        
        