import { ListNode } from './ListNode';  

function rotateRight(head: ListNode | null, k: number): ListNode | null {
    // Edge cases
    if (!head || !head.next || k === 0) {
        return head;
    }
    
    // Find length and last node
    let length = 1;
    let current = head;
    while (current.next) {
        current = current.next;
        length++;
    }
    
    // Calculate effective rotations
    k = k % length;
    if (k === 0) {
        return head;
    }
    
    // Find new tail (at position length - k - 1)
    let newTail = head;
    for (let i = 0; i < length - k - 1; i++) {
        newTail = newTail.next!;
    }
    
    // New head is next to new tail
    const newHead = newTail.next;
    
    // Break the link
    newTail.next = null;
    
    // Connect old tail to old head
    current.next = head;
    
    return newHead;
}

