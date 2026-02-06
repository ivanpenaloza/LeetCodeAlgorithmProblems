import { TreeNode } from './TreeNode'; 

function isSymmetric(root: TreeNode | null): boolean {
    if (!root) return true;
    return checkMirror(root, root);
}

function checkMirror(root1: TreeNode | null, root2: TreeNode | null): boolean {
    if (root1 === null && root2 === null) {
        return true;
    } else if (root1 !== null && root2 !== null) {
        if (root1.val !== root2.val) {
            return false;
        } else {
            return checkMirror(root1.left, root2.right) 
                   && checkMirror(root1.right, root2.left);
        }
    } else {
        return false;
    }
}



