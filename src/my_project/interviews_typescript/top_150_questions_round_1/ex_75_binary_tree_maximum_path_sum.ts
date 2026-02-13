import { TreeNode } from './TreeNode';

function maxPathSum(root: TreeNode | null): number {
    let maxSum = -Infinity;
    
    function dfs(node: TreeNode | null): number {
        /**
         * Returns the maximum path sum that can be extended to the parent.
         * Updates maxSum with the maximum path sum through this node.
         */
        if (!node) {
            return 0;
        }
        
        // Get maximum contribution from left and right subtrees
        // Use Math.max with 0 to ignore negative paths
        const leftMax = Math.max(0, dfs(node.left));
        const rightMax = Math.max(0, dfs(node.right));
        
        // Maximum path sum through this node (can't be extended upward)
        const pathThroughNode = node.val + leftMax + rightMax;
        
        // Update global maximum
        maxSum = Math.max(maxSum, pathThroughNode);
        
        // Return maximum path that can be extended to parent
        // Can only choose one direction (left or right)
        return node.val + Math.max(leftMax, rightMax);
    }
    
    dfs(root);
    return maxSum;
}
