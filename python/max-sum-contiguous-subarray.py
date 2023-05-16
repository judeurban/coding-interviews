'''
task

Find the contiguous subarray within an array, A of length N which has the largest sum.

https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

Example Input
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output
6

Explanation
The subarray [4, -1, 2, 1] has the maximum possible sum of 6.

'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A : tuple):

        current_sum = A[0]
        max_sum = current_sum

        for idx in range(1, len(A), 1):
            current_sum = max(A[idx], current_sum + A[idx])
            max_sum = max(current_sum, max_sum)

        return max_sum

s = Solution()
result = s.maxSubArray(A = [1, 2, 3, 4, -10]) # returns 10
result = s.maxSubArray(A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]) # returns 6
result = s.maxSubArray(A = [20, 1, 1, 1, 1, 1, -400, 1000, 0, -500, 0]) # returns 1000
