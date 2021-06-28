/**
 * https://leetcode.com/problems/intersection-of-two-linked-lists/
 * Using linked list
 */
//1. My Solution
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = 0;
        int lenB = 0;
        
        ListNode currA = headA;
        ListNode currB = headB;
        
        while (currA != null) {
            lenA += 1;
            currA = currA.next;
        }
        
        while (currB != null) {
            lenB += 1;
            currB = currB.next;
        }
        
        if (lenA > lenB) {
            currA = headB;
            currB = headA;
            int temp = lenA;
            lenA = lenB;
            lenB = temp;
        } else {
            currA = headA;
            currB = headB;
        }
        
        for (int i = 0; i < lenB - lenA; i++) {
            currB = currB.next;
        }
        
        while (currA != currB) {
            currA = currA.next;
            currB = currB.next;
        }
        
        return currA;
            
    }
}

//2. Other Solution using hash
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> nodesInB = new HashSet<ListNode>();

        while (headB != null) {
            nodesInB.add(headB);
            headB = headB.next;
        }

        while (headA != null) {
            // if we find the node pointed to by headA,
            // in our set containing nodes of B, then return the node
            if (nodesInB.contains(headA)) {
                return headA;
            }
            headA = headA.next;
        }

        return null;
    }
}
