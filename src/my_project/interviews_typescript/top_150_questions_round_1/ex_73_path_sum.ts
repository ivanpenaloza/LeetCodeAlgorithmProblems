import { TreeNode } from './TreeNode';

export function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (!root) {
        return false;
    }
    if (!root.left && !root.right && root.val === targetSum) {
        return true;
    }
    const tempTarget = targetSum - root.val;
    return hasPathSum(root.left, tempTarget) || hasPathSum(root.right, tempTarget);
}