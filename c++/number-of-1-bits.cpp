/*
task: https://www.interviewbit.com/problems/number-of-1-bits/

Write a function that takes an integer and returns the number of 1 bits it has.

*/

#include <vector>
#include <iostream>

using namespace std;

class Solution
{
    public:
    int numSetBits(unsigned int);
};

int Solution::numSetBits(unsigned int A)
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


int main(int argc, char* argv[])
{
    Solution solution;
    cout << to_string(solution.numSetBits(0xf)) << endl;
    cout << to_string(solution.numSetBits(0x10)) << endl;

    return EXIT_SUCCESS;
}