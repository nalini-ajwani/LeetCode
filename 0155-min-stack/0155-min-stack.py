class MinStack(object):

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stk.append(val)
        if not self.minstk or val <= self.minstk[-1]:
            self.minstk.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stk:
            popped = self.stk.pop()
            if popped == self.minstk[-1]:
                self.minstk.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stk:
            return self.stk[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstk:
            return self.minstk[-1]  # Return the top value from the min stack
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()