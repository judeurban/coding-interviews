'''

task: https://www.interviewbit.com/problems/move-zeroes/

Problem Description
Given an integer array A, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

First argument is array of integers A.


Output Format
Return an array of integers which satisfies above property.

Input 1:
A = [0, 1, 0, 3, 12]

Ouput 1:
[1, 3, 12, 0, 0]

Input 2:
A = [0]

Ouput 2:
[0]

'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        n = len(A)

        non_zero_num_insert_idx = 0

        # populate the first section of the array with non-zero elements
        for source_idx in range(n):

            # put a non zero element at the insert index location
            if A[source_idx] != 0:
                A[non_zero_num_insert_idx] = A[source_idx]
                non_zero_num_insert_idx += 1

        # pad the remaining array with zeros
        for i in range(non_zero_num_insert_idx, n):
            A[i] = 0

        return A

s = Solution()
result = s.solve(A = [0, 1, 0, 3, 12])
expected_result = [1, 3, 12, 0, 0]
print(result == expected_result)

result = s.solve(A = [0])
expected_result = [0]
print(result == expected_result)

result = s.solve(A = [ 0, 0, 9, 4, 0, 10, 3, 8, 6, 2, 6 ])
expected_result = [9, 4, 10, 3, 8, 6, 2, 6, 0, 0, 0]
print(result == expected_result)
