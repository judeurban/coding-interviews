/*
task

Find the contiguous subarray within an array, A of length N which has the largest sum.

https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

Example Input
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output
6

Explanation
The subarray [4, -1, 2, 1] has the maximum possible sum of 6.

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
    int maxSubArray(const vector<int>&);
};

int Solution::maxSubArray(const vector<int> &A)
{
    // hash map between vector and value
    int currentSum = A[0];
    int maxSum = currentSum;

    for(int idx = 1; idx < A.size(); idx++)
    {
        // currentSum = max(A[idx], currentSum + A[idx])
        if(A[idx] >= currentSum + A[idx])
        {
            currentSum = A[idx];
        }
        else
        {
            currentSum += A[idx];
        }

        // maxSum = max(maxSum, currentSum)
        if(currentSum > maxSum)
        {
            maxSum = currentSum;
        }
    }

    return maxSum;
}

int main(int argc, char* argv[])
{

    Solution solution;
    
    vector<int> v1({1, 2, 3, 4, -10});
    vector<int> v2({-2, 1, -3, 4, -1, 2, 1, -5, 4});
    vector<int> v3({20, 1, 1, 1, 1, 1, -400, 1000, 0, -500, 0});

    cout << to_string(solution.maxSubArray(v1)) << endl;
    cout << to_string(solution.maxSubArray(v2)) << endl;
    cout << to_string(solution.maxSubArray(v3)) << endl;

    return EXIT_SUCCESS;
}