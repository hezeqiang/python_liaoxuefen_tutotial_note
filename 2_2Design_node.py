
from json.tool import main

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

    def addAtHead(self, val):
        dummy_head = ListNode(val, next = self)
        return dummy_head
    
    def addAtTail(self, val):
        dummy_head = ListNode(0, next = self)
        cur =  dummy_head.next
        while(cur.next != None):
            cur = cur.next
        
        cur.next = ListNode(val)

        return dummy_head.next

    def addAtIndex(self, index: int, val):
        dummy_head = ListNode(100, next = self)
        cur = dummy_head.next
        newNode = ListNode(val)
        index -= 2
        while(index):
            index -= 1
            if (cur.next != None):
                cur = cur.next
            else:
                return -1
        
        newNode.next = cur.next
        cur.next = newNode

        return dummy_head.next

    def deleteAtIndex(self, index: int):
        dummy_head = ListNode(100, next = self)
        cur = dummy_head.next
        index -= 1

        if index == 0:
            return cur.next

        while (index-1):
            index -= 1
            if (cur.next != None):
                cur = cur.next
            else:
                return -1

        if cur.next.next != None:
            cur.next = cur.next.next
        else:
            cur.next = None

        return dummy_head.next


if __name__ == "__main__":
    
    exam1 = ListNode(5)
    exam2 = ListNode(10)
    exam3 = ListNode(4)
    exam1.next = exam2
    exam2.next = exam3


    #print(exam1.get(1))
    #a = exam1.deleteAtIndex(1)
    a = exam1.deleteAtIndex(2)
    print(a.get(2))
    #print(a.next.val,a.next.next.val, a.next.next.next.val)
    #nexam1=exam1.addAtHead(-2)
    #print(nexam1.get(1))
    #nnexam1=nexam1.addAtTail(-9)
    #print(nnexam1.get(5))

