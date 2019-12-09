class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if low == high:
                if target > nums[low]:
                    return low + 1
                else:
                    return low
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return None
