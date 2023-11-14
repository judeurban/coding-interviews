class Solution:
    # @param A : list of integers
    # @return an integer

    def maxArr(self, A):
        
        max_sum = float('-inf')  # Represents the maximum sum of A[i] + i encountered so far
        max_diff = float('-inf') # Represents the maximum difference of A[i] - i encountered so far
        min_sum = float('inf')   # Represents the minimum sum of A[i] + i encountered so far
        min_diff = float('inf')  # Represents the minimum difference of A[i] - i encountered so far

        for i in range(len(A)):

            max_sum = max(max_sum, A[i] + i)
            max_diff = max(max_diff, A[i] - i)
            min_sum = min(min_sum, A[i] + i)
            min_diff = min(min_diff, A[i] - i)

        return max(max_sum - min_sum, max_diff - min_diff)


solution = Solution()
print(solution.maxArr([ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ]))