from typing import List, Union, Collection, Mapping, Optional


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        """
        Example: nums = [3, 1, 2, 4], costs = [1, 2, 3, 4]
        
        From index 0 (value=3):
          - Next smaller: index 1 (value=1)
          - Next larger: index 3 (value=4)
        
        DP builds cost backwards:
        - dp[3] = 0 (at end, no cost)
        - dp[2] = dp[3] + costs[3] = 0 + 4 = 4 (can jump to 4)
        - dp[1] = dp[2] + costs[2] = 4 + 3 = 7 (can jump to 2)
        - dp[0] = min(dp[1]+costs[1], dp[3]+costs[3]) = min(7+2, 0+4) = 4
        """
        
        smallStack = []  # Monotonic increasing (next smaller element)
        largeStack = []  # Monotonic decreasing (next larger element)
        dp = [0] * len(nums)  # dp[i] = min cost from i to end
        
        # Process backwards (right to left)
        for i in range(len(nums) - 1, -1, -1):
            
            # Maintain monotonic increasing stack (for next smaller)
            # Remove elements >= current (they can't be "next smaller")
            while smallStack and nums[smallStack[-1]] >= nums[i]:
                smallStack.pop()
            
            # Maintain monotonic decreasing stack (for next larger)
            # Remove elements < current (they can't be "next larger")
            while largeStack and nums[largeStack[-1]] < nums[i]:
                largeStack.pop()
            
            # Calculate minimum cost for this position
            nxtCost = []
            
            if largeStack:
                lid = largeStack[-1]  # Next larger index
                nxtCost.append(dp[lid] + costs[lid])
            
            if smallStack:
                sid = smallStack[-1]  # Next smaller index
                nxtCost.append(dp[sid] + costs[sid])
            
            # Min cost from current position to end
            dp[i] = min(nxtCost) if nxtCost else 0
            
            # Add current index to both stacks
            largeStack.append(i)
            smallStack.append(i)

        print(smallStack)
        print(largeStack)
        

        print(dp)
        
        return dp[0]  # Minimum cost from start