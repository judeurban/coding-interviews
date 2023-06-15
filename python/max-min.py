'''
task: https://www.interviewbit.com/problems/max-min-05542f2f-69aa-4253-9cc7-84eb7bf739c4/

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the sum Maximum and Minimum element in the given array.

'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        largest_num = float('-inf')
        smallest_num = float('inf')
        
        for number in A:

            largest_num = max(largest_num, number)
            smallest_num = min(smallest_num, number)

        return largest_num + smallest_num

s = Solution()

result = s.solve(A = [-2, 1, -4, 5, 3])
expected_output = 1
print(result == expected_output)

result = s.solve(A = [1, 3, 4, 1])
expected_output = 5
print(result == expected_output)