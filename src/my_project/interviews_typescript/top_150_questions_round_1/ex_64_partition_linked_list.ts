import { ListNode } from './ListNode';  

function partition(head: ListNode | null, x: number): ListNode | null {
    // Create two dummy nodes for the two partitions
    const lessDummy = new ListNode(0);
    const greaterDummy = new ListNode(0);
    
    // Pointers to build the two lists
    let less = lessDummy;
    let greater = greaterDummy;
    
    // Traverse the original list
    let current = head;
    while (current !== null) {
        if (current.val < x) {
            // Add to the "less than" list
            less.next = current;
            less = less.next;
        } else {
            // Add to the "greater or equal" list
            greater.next = current;
            greater = greater.next;
        }
        current = current.next;
    }
    
    // Important: Set the end of greater list to null
    // to avoid cycles
    greater.next = null;
    
    // Connect the two lists
    less.next = greaterDummy.next;
    
    // Return the head of the combined list
    return lessDummy.next;
}

