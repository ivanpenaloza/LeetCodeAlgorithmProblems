from typing import List, Union, Collection, Mapping, Optional
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        """
        Count k-Free subsets using dynamic programming.
        
        Approach:
        1. Group elements by (num % k) to find independent groups
        2. Within each group, sort and build chains where elements differ by k
        3. For each chain, use House Robber DP to count valid subsets
        4. Multiply results across all independent chains
        
        Time: O(n log n), Space: O(n)
        """
        # Group numbers by their remainder when divided by k
        groups = defaultdict(list)
        for num in nums:
            groups[num % k].append(num)
        
        res = 1
        
        # Process each group independently
        for group in groups.values():
            group.sort()
            
            # Build chains within this group
            i = 0
            while i < len(group):
                chain = [group[i]]
                j = i + 1
                
                # Build chain where each element is exactly k more than previous
                while j < len(group) and group[j] == chain[-1] + k:
                    chain.append(group[j])
                    j += 1
                
                # House Robber DP for this chain
                m = len(chain)
                if m == 1:
                    chain_res = 2  # {} or {chain[0]}
                else:
                    take = 1  # Take first element
                    skip = 1  # Skip first element
                    
                    for idx in range(1, m):
                        new_take = skip  # Can only take current if we skipped previous
                        new_skip = take + skip  # Can skip current regardless
                        take, skip = new_take, new_skip
                    
                    chain_res = take + skip
                
                res *= chain_res
                i = j
        
        return res
        


    

'''
Detailed Algorithm Explanation
Part 1: Why Group by num % k?
Two numbers can have a difference of exactly k only if they have the same remainder when divided by k.

Mathematical proof:

If a - b = k, then a = b + k
Therefore: a % k = (b + k) % k = b % k
Example: nums = [2, 3, 5, 8], k = 5

num | num % 5 | group
----|---------|-------
2   |    2    | Group A
3   |    3    | Group B  
5   |    0    | Group C
8   |    3    | Group B


Why this matters: Elements from different groups can never differ by k, so they're independent. We can combine any subset from Group A with any subset from Group B.

Part 2: Building Chains
Within each group, we sort and find chains where consecutive elements differ by exactly k.

Example with Group B: [3, 8]

Sorted: [3, 8]
Check: 8 - 3 = 5 ✓
Chain: 3 → 8

Another example: nums = [1, 6, 11, 21], k = 5 (all have remainder 1)

Sorted: [1, 6, 11, 21]
Check: 6-1=5 ✓, 11-6=5 ✓, 21-11=10 ✗
Chains: [1 → 6 → 11], [21]


Part 3: House Robber DP - The Core Logic
For a chain like [3 → 8], we can't pick both 3 and 8 (they differ by k). This is the House Robber problem: count all subsets where we don't pick adjacent elements.

DP State Variables
take = number of valid subsets that INCLUDE the current element
skip = number of valid subsets that EXCLUDE the current element

DP Transitions
new_take = skip      # To take current, we MUST have skipped previous
new_skip = take + skip  # To skip current, we can take or skip previous

'''    