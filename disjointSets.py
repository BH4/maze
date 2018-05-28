
class disjointSets:
    def __init__(self, n):
        self.sets = [-1]*n
        self.size = n

    # returns true or false as to weather or not a union was preformed
    def union(self, a, b):  # union by size
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # union was not preformed

        newSize = self.sets[rootA]+self.sets[rootB]#size is negative the number of elements of the set

        # rootA has more elements
        if self.sets[rootA] < self.sets[rootB]:
            self.sets[rootB] = rootA
            self.sets[rootA] = newSize
        else:  # B has more or same
            self.sets[rootA] = rootB
            self.sets[rootB] = newSize

        self.size -= 1

        return True  # union was preformed

    def find(self, a):  # finds root of element with id 'a'
        # also make the parents of this node the root in order to decrease tree height

        parent = self.sets[a]
        if parent < 0:
            return a

        root = self.find(parent)

        self.sets[a] = root

        return root
