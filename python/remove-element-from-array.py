'''
task: https://www.interviewbit.com/problems/remove-element-from-array/

Given an array A and a value B, remove all the instances of that value in the array.
Also, return the number of elements left in the array after the operation. It does not matter what is left beyond the expected length.
Try to do it in less than linear additional space complexity.

Input Format
The first argument is an integer array A.
The second argument is an integer B.

Output Format
Return an integer denoting the number of elements left in the array after the operation, also update the given array A.

Example Input
A = [4, 1, 1, 2, 1, 3]
B = 1

Example Output
Length  : 3 
Array A : [4, 2, 3] 

Example Explanation
If array A is [4, 1, 1, 2, 1, 3]
and the value element is 1,
then the new length is 3, and A is now [4, 2, 3]
'''

class Solution:
    # @param A : list of integers   
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):

        n = len(A)
        b_counts = 0

        right_pointer = n - 1
        left_pointer = 0

        while left_pointer <= right_pointer:

            if A[left_pointer] == B:

                b_counts += 1

                while A[right_pointer] == B and left_pointer <= right_pointer:
                    right_pointer -= 1

                A[left_pointer], A[right_pointer] = A[right_pointer], A[left_pointer]

                right_pointer -= 1
            left_pointer += 1

        for idx in range(n - 1, (n-2) - b_counts, -1):
            del A[idx]

        return (n-1) - b_counts


s = Solution()

expected_result = 3
A = [4, 1, 1, 2, 1, 3]
result = s.removeElement(A, B = 1)
print(expected_result == result)
