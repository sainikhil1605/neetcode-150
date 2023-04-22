/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp=head;
        int c=0;
        while(head!=null){
            head=head.next;
            c++;
        }
        head=temp;
        int l=c-n;
        if(l==0){
            return head.next;
        }
        while(head!=null && l>1){
            head=head.next;
            l--;
        }
        if(head.next==null){
            return null;
        }
        head.next=head.next.next;
        return temp;
    }
}