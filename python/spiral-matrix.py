
class Solution:
	
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):

        # dynmaic variables that indicate the length of iterations that need to be performed for each dimension
        num_rows = len(A[:])
        num_cols = len(A[0])

        top_idx = 0
        bottom_idx = num_rows - 1
        left_idx = 0
        right_idx = num_cols - 1

        result = []
        while top_idx <= bottom_idx and left_idx <= right_idx:

            # traverse the topmost row
            for i in range(left_idx, right_idx + 1):
                result.append(A[top_idx][i])

            top_idx += 1

            # traverse rightmost column
            for i in range(top_idx, bottom_idx + 1):
                result.append(A[i][right_idx])

            right_idx -= 1

            # check remaining cols / rows
            if top_idx <= bottom_idx:

                # traverse bottom row
                for i in range(right_idx, left_idx - 1, -1):
                    result.append(A[bottom_idx][i])

                bottom_idx -= 1
                
            if left_idx <= right_idx:

                for i in range(bottom_idx, top_idx - 1, -1):
                    result.append(A[i][left_idx])

                left_idx += 1
            
        return result


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