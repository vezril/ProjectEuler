#!/usr/bin/env python
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

class Permutation:
    def __init__(self, l):
        self.l = l
        self.position = 0
        self.max_pos = len(self.l)

    def __iter__(self):
        return self

    def next(self):
        if self.position == 0:
            self.position = 1
            return self.l
        elif self.position != self.max_pos:
            tmp_pos = self.position
            while(self.position < 0):
                temp = self.l[self.position]
                self.l[self.position] = self.l[0]
                self.l[0] = temp
                self.position -= 1
            self.position = tmp_pos -= 1
        else:
            raise StopIteration()


if __name__ == "__main__":
    l = ['1','2','3','4']
    p = Permutation(l)
