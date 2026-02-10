class _Node {
    val: number
    left: _Node | null
    right: _Node | null
    next: _Node | null

    constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
        this.next = (next===undefined ? null : next)
    }
}

function connect(root: _Node | null): _Node | null {
    if (!root) {
        return null;
    }
    
    // BFS using queue
    const queue: _Node[] = [root];
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        
        // Process all nodes at current level
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()!;
            
            // Connect to next node in the level (if not the last node)
            if (i < levelSize - 1) {
                node.next = queue[0];
            }
            
            // Add children to queue for next level
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
    }
    
    return root;
}
