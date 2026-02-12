import { TreeNode } from './TreeNode';

function sumNumbers(root: TreeNode | null): number {
    function dfs(node: TreeNode | null, currentNum: number): number {
        if (!node) {
            return 0;
        }
        
        // Build the number by multiplying previous by 10 and adding current digit
        currentNum = currentNum * 10 + node.val;
        
        // If leaf node, return the complete number
        if (!node.left && !node.right) {
            return currentNum;
        }
        
        // Recursively process left and right subtrees
        return dfs(node.left, currentNum) + dfs(node.right, currentNum);
    }
    
    return dfs(root, 0);
}
