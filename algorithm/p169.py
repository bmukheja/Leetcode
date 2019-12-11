class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current = None
        for num in nums:
            if count == 0:
                current = num
            count += (1 if num == current else -1)
        return current