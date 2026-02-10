import { TreeNode } from './TreeNode'; 
            
function flatten(root: TreeNode | null): void {
    if (!root) {
        return;
    }
    
    let current: TreeNode | null = root;
    
    while (current) {
        if (current.left) {
            // Find the rightmost node in the left subtree
            let rightmost: TreeNode = current.left;
            while (rightmost.right) {
                rightmost = rightmost.right;
            }
            
            // Save the current right subtree
            // Connect it to the rightmost node of left subtree
            rightmost.right = current.right;
            
            // Move the left subtree to the right
            current.right = current.left;
            current.left = null;
        }
        
        // Move to the next node
        current = current.right;
    }
}
