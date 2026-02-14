import { TreeNode } from './TreeNode';        

class BSTIterator {
    private stack: TreeNode[];

    constructor(root: TreeNode | null) {
        this.stack = [];
        this.pushLeft(root);
    }

    private pushLeft(node: TreeNode | null): void {
        /**
         * Push all left children of a node onto the stack.
         */
        while (node !== null) {
            this.stack.push(node);
            node = node.left;
        }
    }

    next(): number {
        // Pop the top node (next smallest element)
        const node = this.stack.pop()!;
        
        // If it has a right child, push all left descendants of the right child
        if (node.right !== null) {
            this.pushLeft(node.right);
        }
        
        return node.val;
    }

    hasNext(): boolean {
        return this.stack.length > 0;
    }
}