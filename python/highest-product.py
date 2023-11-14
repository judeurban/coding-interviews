'''
Task:

Given an array A, of N integers A.
Return the highest product possible by multiplying 3 numbers from the array.
NOTE: The solution will fit in a 32-bit signed integer.

Problem Constraints
3 <= N <= 5*105

Input Format
The first and the only argument is an integer array A.

Output Format
Return the highest possible product.

https://www.interviewbit.com/problems/highest-product/

'''

class Solution:
	# @param A : list of integers
	# @return an integer
    def maxp3(self, A):

        NUM_PRODUCTS = 3
        highest_product = 1

        # remove any zeros from the list to prevent destorying the result
        if 0 in A: A.remove(0)

        # create A list containing absolute value
        A_abs = [abs(element) for element in A]

        # sort the lists so we can pop three off
        A = A.sort()
        A_abs = A_abs.sort()

        for i in range(NUM_PRODUCTS):
            highest_number = max(A)
            A.remove(highest_number)
            highest_product *= highest_number

        return highest_product