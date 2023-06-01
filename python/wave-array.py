'''
task: https://www.interviewbit.com/problems/wave-array/

Given an array of integers A, sort the array into a wave-like array and return it. 
In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5..... 

'''

class Solution:
	
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        
        n = len(A)

        # sort so that everything is in ascending order
        A.sort()

        wave_array = list()

        # sort through each number pair, where there will be a smaller number and a larger number
        for idx in range(0, n - 1, 2):

            small_number = A[idx + 0]
            large_number = A[idx + 1]

            wave_array.append(large_number)
            wave_array.append(small_number)

        # if the array has an odd number of elements, the last number should be appended
        if n % 2 != 0:
            wave_array.append(A[-1])

        return wave_array

s = Solution()
print(s.wave(A = [1, 2, 3, 4]))
print(s.wave(A = [1, 2]))
print(s.wave(A = [5, 1, 3, 2, 4]))