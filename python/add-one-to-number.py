'''
task

Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: 
for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

Input Format
First argument is an array of digits.

Output Format
Return the array of digits after adding one.

Example Input
[1, 2, 3]

Example Output
[1, 2, 4]

Example Explanation

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        # cast the array as a string, then do math, then return it as a list

        original_number_string_representation = ""
        for number in A:
            original_number_string_representation = original_number_string_representation + str(number)

        # do some math
        original_number = int(original_number_string_representation)

        new_number_string_representation = str(original_number + 1)

        result = []
        for character in new_number_string_representation:
            result.append(int(character))

        return result

solution = Solution()
print(solution.plusOne(A = [ 0 ]))
print(solution.plusOne(A = [ 9, 9, 9, 9, 9 ]))
