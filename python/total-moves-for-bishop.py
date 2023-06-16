'''
task: https://www.interviewbit.com/problems/total-moves-for-bishop/

Problem Description:
Given the position of a Bishop (A, B) on an 8 * 8 chessboard.
Your task is to count the total number of squares that can be visited by the Bishop in one move.
The position of the Bishop is denoted using row and column number of the chessboard.

Args:
First argument is an integer A denoting the row number of the bishop.
Second argument is an integer B denoting the column number of the bishop.

Output Format
Return an integer denoting the total number of squares that can be visited by the Bishop in one move.

Example Input
A = 4
B = 4

Example Output
13

'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        BOARD_SIZE = 8

        distance_to_right = BOARD_SIZE - B
        distance_to_bottom = BOARD_SIZE - A
        distance_to_left = B - 1
        distance_to_top = A - 1

        return  min(distance_to_right, distance_to_bottom) + \
                min(distance_to_bottom, distance_to_left) + \
                min(distance_to_left, distance_to_top) + \
                min(distance_to_top, distance_to_right)

s = Solution()

result = s.solve(
    A = 4,
    B = 4
)
expected_result = 13
print(expected_result == result)