import { TreeNode } from './TreeNode';

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (p && q) {
        return p.val === q.val 
               && isSameTree(p.left, q.left) 
               && isSameTree(p.right, q.right);
    } else {
        return p === q;
    }
}
