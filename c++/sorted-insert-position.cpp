/*
task: https://www.interviewbit.com/problems/sorted-insert-position/

Problem Description

Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Problem Constraints
1 <= |A| <= 100000
1 <= B <= 109

Input Format
First argument is array A.
Second argument is integer B.

Output Format
Return an integer, the answer to the problem.

Example Input

Input 1:
A = [1, 3, 5, 6]
B = 5

Input 2:
A = [1, 3, 5, 6]
B = 2

Example Output
Output 1:
2

Output 2:
1

Example Explanation
Explanation 1:

5 is found at index 2.
Explanation 2:

2 will be inserted ar index 1.

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
    int searchInsert(vector<int> &A, int B);
};

int Solution::searchInsert(vector<int>& A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    int startingIdx = 0;
    int endingIdx = A.size() - 1;

    while (startingIdx <= endingIdx) {

        int middleIdx = startingIdx + (endingIdx - startingIdx) / 2;

        if(A.at(middleIdx) == B)
        {
            return middleIdx;
        }
        else if (A.at(middleIdx) < B)
        {
            startingIdx = middleIdx + 1;
        }
        else {
            endingIdx = middleIdx - 1;
        }
    }

    return startingIdx;
}


int main(int argc, char* argv[])
{
    Solution solution;
    vector<int> A = {1, 3, 5, 6};
    int B;

    B = 5;
    cout << solution.searchInsert(A, B) << endl;             // returns 2

    B = 2;
    cout << solution.searchInsert(A, B) << endl;             // returns 1

    return EXIT_SUCCESS;
}