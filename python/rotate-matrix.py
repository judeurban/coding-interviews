'''
task: https://www.interviewbit.com/problems/rotate-matrix/

You are given a N x N 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place. Update the given matrix A.
Note: If you end up using an additional array, you will only receive a partial score.
Problem Constraints
1 <= N <= 1000

Input Format
First argument is a 2D matrix A of integers

Output Format
Rotate the given 2D matrix A.

Example Input
Input 1:
[
    [1, 2],
    [3, 4]
 ]
Input 2:
[
    [1]
]

Example Output

Output 1:
[
    [3, 1],
    [4, 2]
 ]
Output 2:
[
    [1]
]
 Example Explanation
Explanation 1:
After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:
2D array remains the same as there is only element.
'''

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        
        n = len(A)
        
        # transpose the matrix
        for row_idx in range(n):
            for col_idx in range(row_idx + 1, n):
                A[row_idx][col_idx], A[col_idx][row_idx] = A[col_idx][row_idx], A[row_idx][col_idx]

        # reverse the row order
        for i in range(n):
            A[i] = A[i][::-1]
            
        return A


s = Solution()

s.rotate(
    A = [
        [1, 2],
        [3, 4]
    ]
)

s.rotate(
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)