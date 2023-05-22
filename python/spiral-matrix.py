
class Solution:
	
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):

        num_rows = len(A[:])
        num_cols = len(A[0])

        top_row_index = 0
        bottom_row_index = num_rows - 1
        
        left_column_index = 0
        right_column_index = num_cols - 1

        spiral_A = list()

        while top_row_index <= bottom_row_index and left_column_index <= right_column_index:

            # loop thru the topmost row
            for col in range(left_column_index, right_column_index + 1):
                current_num = A[top_row_index][col]
                spiral_A.append(current_num)

            top_row_index += 1

            # loop thru the right most column
            for row in range(top_row_index, bottom_row_index + 1):
                current_num = A[row][right_column_index]
                spiral_A.append(current_num)

            right_column_index -= 1

            if top_row_index <= bottom_row_index:

                # loop thru the bottom row
                for col in range(right_column_index, left_column_index - 1, -1):
                    current_num = A[bottom_row_index][col]
                    spiral_A.append(current_num)

                bottom_row_index -= 1

            if left_column_index <= right_column_index:

                # loop thru the left column
                for row in range(bottom_row_index, top_row_index - 1, -1):
                    current_num = A[row][left_column_index]
                    spiral_A.append(current_num)
                
                left_column_index -= 1

        return spiral_A

solution = Solution()

print(solution.spiralOrder(
    [
    [1, 2],
    [3, 4],
    [5, 6]
    ]
))

	
print(solution.spiralOrder(
	    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
))

print(solution.spiralOrder(
	    [[1]]
))