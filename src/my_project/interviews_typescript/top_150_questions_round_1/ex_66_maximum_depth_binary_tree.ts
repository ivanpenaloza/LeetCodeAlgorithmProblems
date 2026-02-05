import { TreeNode } from './TreeNode';

function maxDepth(root: TreeNode | null): number {
    if (!root) {
        return 0;
    } else {
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}

