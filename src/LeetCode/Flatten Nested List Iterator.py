"""
Using 
"""
#1. My Solution (71ms)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = deque(nestedList)
    
    def next(self) -> int:
        return self.list.popleft().getInteger()
        
    
    def hasNext(self) -> bool:
        while self.list and not self.list[0].isInteger():
            first = self.list.popleft().getList()
            for n in first[::-1]:
                self.list.appendleft(n)
        return self.list

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#2. Other Solution (55ms)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque(reversed(nestedList))
        self.val = self._next()
    
    def next(self) -> int:
        val, self.val = self.val, self._next()
        return val

    def _next(self) -> int:
        while self.q:
            x = self.q.pop()
            if x.isInteger():
                return x.getInteger()
            for y in reversed(x.getList()):
                self.q.append(y)
        return None
    
    def hasNext(self) -> bool:
        return self.val is not None
