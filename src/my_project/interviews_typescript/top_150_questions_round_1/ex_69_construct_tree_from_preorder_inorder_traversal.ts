import { TreeNode } from './TreeNode';         

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    // Create a hashmap for quick lookup of indices in inorder
    const inorderMap = new Map<number, number>();
    inorder.forEach((val, idx) => inorderMap.set(val, idx));
    
    let preorderIdx = 0;
    
    function build(left: number, right: number): TreeNode | null {
        // Base case: no elements to construct the tree
        if (left > right) {
            return null;
        }
        
        // Pick the current root from preorder
        const rootVal = preorder[preorderIdx];
        const root = new TreeNode(rootVal);
        
        // Move to the next element in preorder
        preorderIdx++;
        
        // Find the index of root in inorder to split left and right subtrees
        const inorderIdx = inorderMap.get(rootVal)!;
        
        // Build left subtree (all elements before root in inorder)
        root.left = build(left, inorderIdx - 1);
        
        // Build right subtree (all elements after root in inorder)
        root.right = build(inorderIdx + 1, right);
        
        return root;
    }
    
    return build(0, inorder.length - 1);
}

