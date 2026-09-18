class ListNode:
    def __init__(self, val:int):
         self.val = val
         self.next = None
         self.min = 9223372036854775807

class MinStack:
    def __init__(self):
        self.head = ListNode(0)
        self.len = 0
        self.curMin = 9223372036854775807


    def push(self, val: int) -> None:
        n = ListNode(val)
        n.next = self.head.next
        self.head.next = n
        if self.curMin > val or self.curMin == None:
            self.curMin = val
        n.min = min(self.curMin, val)

    def pop(self) -> None:
        # set the head's next to the head's next next
        if self.head.next:
            if self.head.next.min == self.curMin:
                if self.head.next.next:
                    self.curMin = self.head.next.next.min
                else:
                    self.curMin = 9223372036854775807
            if self.head.next.next:
                self.head.next = self.head.next.next
            else:
                self.head.next = None

    def top(self) -> int:
        if self.head.next:
            return self.head.next.val

    def getMin(self) -> int:
        return self.head.next.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()