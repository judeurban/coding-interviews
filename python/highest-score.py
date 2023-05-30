'''
task

https://www.interviewbit.com/problems/highest-score/
'''

class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, A):

        # this solution is O(n) time complexity

        total_sum_map = dict()                    # contains a name: sum mapping
        count_map = dict()                        # contains a name: size mapping
        
        # compute all averages
        for [name, mark_value] in A:

            mark_value = float(mark_value)
            
            if total_sum_map.get(name) == None: 
                total_sum_map[name] = 0
                count_map[name] = 0
            
            total_sum_map[name] += mark_value
            count_map[name] += 1

        highest_average_mark = float('-inf')

        # find the higest average mark
        for name in total_sum_map.keys():

            # calculate the average for this name
            total_sum = total_sum_map[name]
            total_count = count_map[name]

            average = total_sum / total_count
            
            # choose the highest value
            highest_average_mark = max(highest_average_mark, average)

        return int(highest_average_mark)
    
s = Solution()
print(s.highestScore(A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"]]))
print(s.highestScore(A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"], ["Alice", "10"]]))

print(s.highestScore(A = [
  ["smqzg", "91"],
  ["wdpcg", "76"],
  ["eaqs", "95"],
  ["nre", "75"],
  ["jwxvz", "55"],
  ["adfho", "59"],
  ["nre", "9"],
  ["mjgds", "66"],
  ["adfho", "12"],
  ["pewdo", "31"],
  ["cioii", "36"],
  ["smqzg", "99"],
  ["hlzsa", "3"],
  ["rfbug", "22"],
  ["fdn", "57"],
  ["qyxm", "84"],
  ["adfho", "49"],
  ["adfho", "12"],
  ["nre", "43"],
  ["tudsu", "48"],
  ["pynd", "16"],
  ["rfbug", "44"],
  ["xoro", "44"],
  ["tudsu", "62"],
  ["dmmf", "75"],
  ["adfho", "55"],
  ["vlm", "91"],
  ["rmy", "63"],
  ["smqzg", "25"],
  ["lmp", "3"],
  ["mhr", "8"],
  ["rfbug", "60"],
  ["irrea", "35"],
  ["xbbka", "5"],
  ["irrea", "59"],
  ["wdpcg", "73"],
  ["mhr", "24"],
  ["irrea", "11"],
  ["dmmf", "89"],
  ["rfbug", "91"],
  ["oeov", "84"],
  ["wdpcg", "90"],
  ["mjgds", "65"],
  ["irrea", "43"],
  ["pule", "6"],
  ["bxsqq", "0"],
  ["sda", "43"],
  ["adfho", "60"],
  ["caysx", "3"],
  ["muipy", "10"],
  ["nre", "71"],
  ["kxj", "88"],
  ["muipy", "53"],
  ["rmy", "91"],
  ["smqzg", "94"],
  ["tudsu", "10"],
  ["dmmf", "46"],
  ["xcri", "91"],
  ["pynd", "84"],
  ["caysx", "85"],
  ["vlm", "4"],
  ["yev", "36"],
  ["dmmf", "16"],
  ["caysx", "79"],
  ["adfho", "23"],
  ["bin", "16"],
  ["eaqs", "15"],
  ["mjgds", "87"],
  ["adfho", "87"],
  ["vlm", "61"],
  ["eaqs", "61"],
  ["qhtz", "40"],
  ["ghl", "13"],
  ["qyxm", "79"],
  ["lmp", "81"],
  ["mhr", "58"],
  ["vlm", "49"],
  ["fdn", "48"],
  ["eaqs", "8"],
  ["jwxvz", "99"],
  ["fdn", "74"],
  ["pewdo", "27"],
  ["ghl", "82"],
  ["ghl", "44"],
  ["fdn", "96"],
  ["yev", "8"],
  ["bxsqq", "99"],
  ["pynd", "83"],
  ["xbbka", "37"],
  ["pule", "41"],
  ["rmy", "79"],
  ["xoro", "31"],
  ["qhtz", "4"],
  ["smqzg", "64"],
  ["dmmf", "27"],
  ["kxj", "43"],
  ["nre", "1"],
  ["smqzg", "70"],
  ["lmp", "73"],
  ["mhr", "93"],
  ["pybh", "82"],
  ["adfho", "89"],
  ["hlzsa", "7"],
  ["pynd", "60"],
  ["vlm", "14"]]
))