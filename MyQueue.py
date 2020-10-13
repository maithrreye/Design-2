"""
Time complexity O(1) for Push, Pop, peek and empty
Space Complexity O(1)


Did this code successfully run on Leetcode : Yes 
Any problem you faced while coding this : No 

"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Q=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.Q.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.Q.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.Q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.Q)==0:
            return True
        else:
            return False
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()