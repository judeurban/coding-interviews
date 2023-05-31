/*
task: https://www.interviewbit.com/problems/count-total-set-bits/

Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

Return the count modulo 109 + 7.

*/

#include <vector>
#include <iostream>

using namespace std;

const int MOD = 1000000007;  // 10^9 + 7

class Solution
{
    public:
    int solve(int);
    // int numSetBits(int);
};

int numSetBits(int A)
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    uint8_t numHighBits = 0;
    unsigned int sliderBit = 0x1; // this is the first bit, then I'll multiply by 2 to left shift the bit
    const uint8_t numBits = sizeof(A) * 8;

    for(uint8_t i = 0; i < numBits; i++)
    {
        // there is a one at this bit
        if(sliderBit == (A & sliderBit))
        {
            numHighBits++;
        }

        // slide the bit left over by one
        sliderBit = sliderBit << 1;
    }

    return numHighBits;
}


int Solution::solve(int A)
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    uint16_t totalSum = 0;

    for(int i = 0; i <= A; i++)
    {
        uint8_t numHighBits = numSetBits(i);
        totalSum += numHighBits;
    }

    return totalSum % MOD;
}


int main(int argc, char* argv[])
{
    Solution solution;
    cout << to_string(solution.solve(3)) << endl;
    cout << to_string(solution.solve(1)) << endl;

    return EXIT_SUCCESS;
}