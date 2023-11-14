'''
task: https://www.interviewbit.com/problems/set-intersection/

Problem Description

An integer interval [X, Y] (for integers X < Y) is a set of all consecutive integers from X to Y, including X and Y.
You are given a 2D array A with dimensions N x 2, where each row denotes an interval.
Find the minimum size of a set S such that for every integer interval Z in A, the intersection of S with Z has a size of at least two.

Input 1:
A = [[1, 3], [1, 4], [2, 5], [3, 5]]

Input 2:
A = [[1, 2], [2, 3], [2, 4], [4, 5]]

Output 1:
3

Output 2:
5

Example Explanation
Explanation 1:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.

Explanation 2:
An example of a minimum sized set is {1, 2, 3, 4, 5}.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    # def setIntersection(self, A):

    #     seen_numbers = set()
    #     global_intersection = set()
    #     len(seen_numbers)
        
    #     # collect all unique numbers
    #     for interval in A:
    #         for number in interval:
                
    #             if number not in seen_numbers:
    #                 seen_numbers.add(number)

    #     global_intersection = seen_numbers.copy()

    #     # collect the intersection between ALL numbers and the numbers in the intersection
    #     for interval in A:
    #         for number in interval:

    #             global_intersection.intersection(interval)
    #             print(global_intersection)

    def setIntersection(self, A):

        A.sort()   # Sort the intervals based on start points
        s = set()  # Set S to store elements
        
        for interval in A:

            # Check intersection size
            if len(s & set(range(interval[0], interval[1] + 1))) < 2:
                
                s.add(interval[1])  # Add last element of interval to S
        
        return len(s)

s = Solution()

result = s.setIntersection(A = [[1, 3], [1, 4], [2, 5], [3, 5]])
expected_result = 3
print(result == expected_result)

result = s.setIntersection(A = [[1, 2], [2, 3], [2, 4], [4, 5]])
expected_result = 5
print(result == expected_result)
