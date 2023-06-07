'''
task

https://www.interviewbit.com/problems/noble-integer/

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.

'''

class Solution:
# @param A : list of integers
# @return an integer
    def solve(self, A):

        n = len(A)

        # sort the array in ascending order 
        A.sort()
        n = len(A)

        for i, number in enumerate(A):

            # you cannot have a negative count
            if number < 0:
                continue

            j = i
            while j < n - 1 and A[j] == A[j + 1]:
                j += 1

            higher_integer_count = n - 1 - j

            if number == higher_integer_count:
                return 1

        return -1

s = Solution()
print( 1 == s.solve(A = [3, 2, 1, 3]))        # should return 1
print( -1 == s.solve(A = [1, 1, 3, 3]))        # should return -1
print( 1 == s.solve(A = [5, 6, 2]))           # should return 1

# should return
print(s.solve(A = [ -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7, -4, -10, -4, 2, 6, 1, -2, -3, -1, -8, 0, -8, -7, -3, 5, -1, -8, -8, 8, -1, -3, 3, 6, 1, -8, -1, 3, -9, 9, -6, 7, 8, -6, 5, 0, 3, -4, 1, -10, 6, 3, -8, 0, 6, -9, -5, -5, -6, -3, 6, -5, -4, -1, 3, 7, -6, 5, -8, -5, 4, -3, 4, -6, -7, 0, -3, -2, 6, 8, -2, -6, -7, 1, 4, 9, 2, -10, 6, -2, 9, 2, -4, -4, 4, 9, 5, 0, 4, 8, -3, -9, 7, -8, 7, 2, 2, 6, -9, -10, -4, -9, -5, -1, -6, 9, -10, -1, 1, 7, 7, 1, -9, 5, -1, -3, -3, 6, 7, 3, -4, -5, -4, -7, 9, -6, -2, 1, 2, -1, -7, 9, 0, -2, -2, 5, -10, -1, 6, -7, 8, -5, -4, 1, -9, 5, 9, -2, -6, -2, -9, 0, 3, -10, 4, -6, -6, 4, -3, 6, -7, 1, -3, -5, 9, 6, 2, 1, 7, -2, 5 ]))

# should return 
print(1 == s.solve(A = [ 4, -9, 8, 5, -1, 7, 5, 3 ]))           # should return 1
print(1 == s.solve(A = [ -4, -2, 0, -1, -6 ]))                  # should return 1
