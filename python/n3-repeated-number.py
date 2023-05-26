class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        threshold = int(len(A) / 3)
        num_count_hashmap = dict()

        for number in A:

            # first occurance of this number
            if num_count_hashmap.get(number) == None:
                num_count_hashmap[number] = 1
            
            # number exists in the hashmap already
            else:
                num_count_hashmap[number] += 1

            
            if num_count_hashmap[number] > threshold:
                return number
    
        return -1

s = Solution()
print(s.repeatedNumber(A=[1, 2, 3, 1, 1]))