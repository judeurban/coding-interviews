'''
task: https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 

You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Given two integer arrays A and B, where
    - A[i] is x coordinate and
    - B[i] is y coordinate of ith point respectively.

Return an Integer, i.e minimum number of steps.

Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]

Output 1:

 2

Example Explanation
Explanation 1:

 Given three points are: (0, 0), (1, 1) and (1, 2).
 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2)

'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):

        x_coord = A[0]
        y_coord = B[0]

        num_steps = 0
        
        for new_x_coord, new_y_coord in zip(A[1:], B[1:]):

            delta_x = abs(new_x_coord - x_coord)
            delta_y = abs(new_y_coord - y_coord)
            
            num_steps += max(delta_x, delta_y)

            x_coord = new_x_coord
            y_coord = new_y_coord

        return num_steps


s = Solution()
print(
    s.coverPoints(
        A = [0, 1, 1],
        B = [0, 1, 2]
    )
)

print(
    s.coverPoints(
    A = [ -7, -13 ],
    B = [ 1, -5 ]
    )
)