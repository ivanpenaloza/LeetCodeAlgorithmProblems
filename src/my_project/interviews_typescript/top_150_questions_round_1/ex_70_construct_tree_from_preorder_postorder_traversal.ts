import { TreeNode } from './TreeNode'; 

function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    // Create a hashmap for quick lookup of indices in inorder
    const inorderMap = new Map<number, number>();
    inorder.forEach((val, idx) => inorderMap.set(val, idx));
    
    let postorderIdx = postorder.length - 1;
    
    function build(left: number, right: number): TreeNode | null {
        // Base case: no elements to construct the tree
        if (left > right) {
            return null;
        }
        
        // Pick the current root from postorder (from end)
        const rootVal = postorder[postorderIdx];
        const root = new TreeNode(rootVal);
        
        // Move to the previous element in postorder
        postorderIdx--;
        
        // Find the index of root in inorder to split left and right subtrees
        const inorderIdx = inorderMap.get(rootVal)!;
        
        // Build right subtree first (postorder: left → right → root)
        // So when we go backwards, we process root → right → left
        root.right = build(inorderIdx + 1, right);
        
        // Build left subtree
        root.left = build(left, inorderIdx - 1);
        
        return root;
    }
    
    return build(0, inorder.length - 1);
}

