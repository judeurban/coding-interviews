'''
task: https://www.interviewbit.com/problems/find-duplicate-in-array/

Given a read-only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
If there are multiple possible answers ( like in the sample case ), output any one, if there is no duplicate, output -1
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        seen_numbers = set()
        for num in A:

            if num in seen_numbers:
                return num
            
            seen_numbers.add(num)
        
        return -1

s = Solution()

expected_result = 4
result = s.repeatedNumber(A = [3, 4, 1, 4, 2])
print(expected_result == result)

expected_result = -1
result = s.repeatedNumber(A = [1, 2, 3])
print(expected_result == result)

expected_result = 4 # or 1
result = s.repeatedNumber(A = [3, 4, 1, 4, 1])
print(expected_result == result)
