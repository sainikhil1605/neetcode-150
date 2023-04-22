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
    public ListNode merge(ListNode h1,ListNode h2){
        ListNode d=new ListNode(-1);
        ListNode temp=d;
        while(h1!=null && h2!=null){
            d.next=h1;
            h1=h1.next;
            d=d.next;
            d.next=h2;
            d=d.next;
            
            h2=h2.next;
        }
        
        if(h1!=null){
            d.next=h1;
            
        }
        else if(h2!=null){
            d.next=h2;
        }
        return temp.next;
    }
    
    public ListNode reverse(ListNode head){
        if(head.next==null){return head;}
        ListNode x=reverse(head.next);
        head.next.next=head;
        head.next=null;
        return x;
    }
    public void reorderList(ListNode head){
        ListNode temp=head;
        int c=0;
        if(head==null){return ;}
        while(head!=null && head.next!=null){
            head=head.next;
            c++;
        }
        if(c==0){return ;}
        head=temp;
        for(int i=1;i<=c/2;i++)
            head=head.next;
        ListNode head1=head.next;
        head.next=null;
        ListNode x=reverse(head1);
        head=temp;
        head=merge(head,x);
        
    }
}