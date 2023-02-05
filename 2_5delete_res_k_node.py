
from json.tool import main


from sympy import Li

class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        dummy_head = ListNode(100,next = self)
        cur = dummy_head.next
        index -= 1

        while(index):
            index -= 1
            if (cur.next != None):
                cur = cur.next
            else:
                return -1

        return cur.val


class Solution:

    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0, next = head)
        cur = head
        left = ListNode(0, next = head)
        k = k - 1

        for _ in range(k):
            cur = cur.next
            if cur == None:
                return -1


        while (cur.next != None):
            cur = cur.next
            left = left.next
        
        left.next = left.next.next

        return dummy_head.next

if __name__ == "__main__":
    
    exam1 = ListNode(5)
    exam2 = ListNode(10)
    exam3 = ListNode(4)
    exam4 = ListNode(1)
    exam1.next = exam2
    exam2.next = exam3
    exam3.next = exam4

    exam = Solution()
    nexam1 = exam.removeNthFromEnd(exam1,5)
    print(nexam1.get(3))
    #a = exam1.deleteAtIndex(1)
    #print(a.next.val,a.next.next.val, a.next.next.next.val)
    #nexam1=exam1.addAtHead(-2)
    #print(nexam1.get(1))
    #nnexam1=nexam1.addAtTail(-9)
    #print(nnexam1.get(5))

