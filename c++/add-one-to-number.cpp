/*
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

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
    vector<int> plusOne(vector<int> &A);
};


vector<int> Solution::plusOne(vector<int> &A)
{
    A[A.size() - 1] += 1;
    return A;
}

int main(int argc, char* argv[])
{

    Solution solution;
    
    vector<int> A({1, 2, 3}); // we expect {1, 2, 4}
    vector<int> newVector = solution.plusOne(A);

    return EXIT_SUCCESS;
}