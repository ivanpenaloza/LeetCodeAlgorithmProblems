from typing import List, Union, Collection, Mapping, Optional

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        freq_sum = dict()
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            freq_sum[nums[right]] = freq_sum.get(nums[right], 0) + 1

            if right - left > k - 1:
                freq_sum[nums[left]] -= 1
                if freq_sum[nums[left]] == 0:
                    del freq_sum[nums[left]]
                current_sum -= nums[left]
                left += 1

            if right - left == k - 1 and len(freq_sum) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum