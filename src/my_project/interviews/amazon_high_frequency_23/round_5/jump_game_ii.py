from typing import List 

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy approach: At each position, jump to the farthest reachable index
        
        Example: [2,3,1,1,4]
        - From index 0 (value=2): can reach indices 1,2
        - Greedy choice: Jump to index 1 (value=3) because it reaches farthest
        - From index 1: can reach indices 2,3,4 (end)
        - Answer: 2 jumps
        """

        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0 # End of current jump range
        farthest = 0    # The farthest position we can reach

        for i in range(len(nums) - 1):
            # Update farthest position reachable
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest  # Make the greedy choice

                if current_end > len(nums) - 1:
                    break
        return jumps
