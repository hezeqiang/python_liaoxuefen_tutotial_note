
from json.tool import main


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def removeElement(self, head: ListNode ,val: int) -> ListNode:
        dummy_head = ListNode(0,next=head)
        cur = dummy_head
        while(cur.next != None):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next



if __name__ == "__main__":
    
    exam1 = ListNode(5)
    exam2 = ListNode(2)
    exam3 = ListNode(4)
    exam1.next = exam2
    exam2.next = exam3

    ax = Solution()
    a = ax.removeElement(exam1, 5)
    print(a.val)
    #print(a.next.val,a.next.next.val, a.next.next.next.val)
