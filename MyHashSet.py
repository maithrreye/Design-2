"""
Time complexity is O(n) for all opeartion add, remove and contains where n is no of keys stored in the bucket
Space complexity is O(n)

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this :

Space Complexity for this code is confusing. If self.size and idx as Auxillary space , they are variable that hold single value like size and index so can i say O(n) or O(1)??
"""


class MyHashSet:

    def __init__(self):
        """
        List of list with size thousand.
        """
        self.capacity = 1000
        self.bucket= [[] for _ in range(self.capacity)]
        

    def add(self, key: int) -> None:
        """
        Find index using Hash function
        Add the key into the list belonging to that index 
        """
        idx=key% self.capacity
        if key not in self.bucket[idx]:
            self.bucket[idx].append(key)
    
    def remove(self, key: int) -> None:
        """
        Find index using Hash function
        Remove the key from the list belonging to that index 
        """
        idx=key% self.capacity
        if key in self.bucket[idx]:
            self.bucket[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if the list contained the key
        """
        idx=key% self.capacity
        if key in self.bucket[idx]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)