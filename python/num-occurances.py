class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):

        # number: occurances
        number_occurances = dict()
        
        for number in A:
            
            if number in number_occurances.keys():
                number_occurances[number] = number_occurances[number] + 1
            
            # number doesn't exist yet
            else:
                number_occurances[number] = 1
                
        # sort the list based on the key (number)
        export_list = [number_occurances[num] for num in sorted(number_occurances.keys())]                
        return export_list
            
solution = Solution()
print(solution.findOccurences([4, 3, 3]))