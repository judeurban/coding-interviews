/*
task: https://www.interviewbit.com/problems/reverse-bits/


*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
    unsigned int reverse(unsigned int A);
};

unsigned int Solution::reverse(unsigned int A)
{
    int numBits = sizeof(A) * 8;
    unsigned int result = 0x0;                                      // initialize all bits to low
    unsigned int largestSignificantBitHigh  = 0x80000000;           // this bit moves right to left
    unsigned int smallestSignificantBitHigh = 0x00000001;           // this bit moves from left the right

    for(int i = 0; i < numBits; i++)
    {
        unsigned int sourceSliderBit = smallestSignificantBitHigh << i;      // move bit to the left
        unsigned int resultSliderBit = largestSignificantBitHigh >> i;       // move bit to the right

        // A is high at this bit, write a high bit to this location
        if ((A & sourceSliderBit) != 0x0)
        {
            result = result | resultSliderBit;
        }
    }

    return result;
}

int main(int argc, char* argv[])
{
    Solution solution;

    unsigned int a;

    a = 0x0;
    std::cout << hex << solution.reverse(a) << std::endl;       // prints 0x00000000

    a = 0x1;
    std::cout << hex << solution.reverse(a) << std::endl;       // prints 0x80000000

    a = 0x80000000;
    std::cout << hex << solution.reverse(a) << std::endl;       // prints 0x00000001

    a = 0xffffffff;
    std::cout << hex << solution.reverse(a) << std::endl;       // prints 0xffffffff

    return EXIT_SUCCESS;
}