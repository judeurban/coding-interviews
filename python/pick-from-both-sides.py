'''
task: https://www.interviewbit.com/problems/pick-from-both-sides/

Given an integer array A of size N.

You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick the first four elements or can pick the last four elements or can pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick.

First argument is an integer array A.

Second argument is an integer B.

Return an integer denoting the maximum possible sum of elements you picked.

Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3

Output 1:
 8

Input 2:
 A = [1, 2]
 B = 1

Output 2:
 2

'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A: list, B: int):

        # we want to iterate from both ends
        for i in range(B):
            

s = Solution()
print(
    s.solve(
        A = [5, -2, 3 , 1, 2],
        B = 3
    )
)