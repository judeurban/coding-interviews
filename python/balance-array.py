'''
task

Given an integer array A of size N. You need to count the number of special elements in the given array.
A element is special if removal of that element make the array balanced.
Array will be balanced if sum of even index element equal to sum of odd index element.

Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the count of special elements.

Example Input

Input 1:
A = [2, 1, 6, 4]

Input 2:
A = [5, 5, 2, 5, 8]

Example Output

Output 1:
1

Output 2:
2

Example Explanation
Explanation 1:

 After deleting 1 from array : {2,6,4}
    (2+4) = (6)
 Hence 1 is the only special element, so count is 1
Explanation 2:

 If we delete A[0] or A[1] , array will be balanced
    (5+5) = (2+8)
 So A[0] and A[1] are special elements, so count is 2.

 https://www.interviewbit.com/problems/balance-array/
 
 '''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # this solution is O(3*n) which can be assumed to be O(n), which is a linear time comlexity

        n = len(A)

        prefix_even = [0] * n
        prefix_odd = [0] * n

        even_sum = 0
        odd_sum = 0

        isEven = lambda x: x % 2 == 0

        # compute the cumulative sum of both even and odd elements
        for i in range(n):

            if isEven(i):
                even_sum += A[i]
            else:
                odd_sum += A[i]

        print(f'{even_sum=}')
        print(f'{odd_sum=}')

        # compute the prefix sums of even and odd elements
        for i in range(1, n):
            if isEven(i):
                prefix_even[i] = prefix_even[i-1] + A[i]
                prefix_odd[i] = prefix_odd[i-1]
            else:
                prefix_even[i] = prefix_even[i-1]
                prefix_odd[i] = prefix_odd[i-1] + A[i]

        print(f'{prefix_even=}')
        print(f'{prefix_odd=}')

        special_number_count = 0

        # Check for indices that satisfy the conditions
        for i in range(n):
            left_sum = prefix_even[i-1] + prefix_odd[n-1] - prefix_odd[i]
            right_sum = prefix_odd[i-1] + (even_sum - prefix_even[i])

            if left_sum == right_sum:
                special_number_count += 1

        return special_number_count

s = Solution()
print(s.solve([2, 1, 6, 4]))
print(s.solve([5, 5, 2, 5, 8]))
