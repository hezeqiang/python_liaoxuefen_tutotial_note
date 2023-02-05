
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
    
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prenode = ListNode(0)
        prenode.next = None
        tempnode = ListNode(0)

        while (cur != None):
            tempnode.next = cur.next
            cur.next = prenode
            prenode = cur    
            cur = tempnode.next

        return prenode


    def res_two(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0, next = head)
        cur = dummy_head

        while (cur.next.next):
            print(cur.next.next.val)
            tempnode1 = cur.next.next.next
            tempnode2 = cur.next.next
            cur.next.next.next = cur.next
            cur.next = tempnode2
            cur = cur.next.next
            cur.next = tempnode1
            if tempnode1 == None: # in case that cur.next not exist in next loop
                break

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
    nexam1 = exam.res_two(exam1)
    print(nexam1.get(3))
    #a = exam1.deleteAtIndex(1)
    #print(a.next.val,a.next.next.val, a.next.next.next.val)
    #nexam1=exam1.addAtHead(-2)
    #print(nexam1.get(1))
    #nnexam1=nexam1.addAtTail(-9)
    #print(nnexam1.get(5))

