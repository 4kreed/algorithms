"""
Implementation of Set
"""
import itertools
import math

class Set(frozenset):
    """
    Definition of a Set
    It's important that Set be a subclass of frozenset, (not set), because:
    1) it makes Set immutable
    2) it allows Set to contains Sets
    """
    def __repr__(self):
        return str(set(self))

    def __str__(self):
        return str(set(self))

    def __add__(self, other):
        """
        Returns the union of self and other.

        Args:
            other : instance of Set.
        """
        if not isinstance(other, Set):
            raise TypeError("One of the objects is not a set")

        #return Set(self.union(other))
        return Set(self | other)

    union = __add__


    def __sub__(self, other):
        """
        Returns the difference of self and other.

        Args:
            other : instance of Set.
        """
        if not isinstance(other, Set):
            raise TypeError("One of the objects is not a set")

        #return Set(self.union(other))
        return Set(self.difference(other))

    Difference = __sub__
