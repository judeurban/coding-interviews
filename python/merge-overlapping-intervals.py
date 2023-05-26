'''
task

Given a collection of intervals, merge all overlapping intervals.

Problem Constraints
1 <= Total number of intervals <= 100000.

Input Format
First argument is a list of intervals.

Output Format
Return the sorted list of intervals after merging all the overlapping intervals.

Example Input
[1,3],[2,6],[8,10],[15,18]

Example Output
[1,6],[8,10],[15,18]

Example Explanation

Merge intervals [1,3] and [2,6] -> [1,6].
so, the required answer after merging is [1,6],[8,10],[15,18].
No more overlapping intervals present.

https://www.interviewbit.com/problems/merge-overlapping-intervals/


'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        
        # sort the intervals based on the start to 
        # ensure that all invervals are adjacent to each other
        intervals.sort(key=lambda x: x.start)
        
        result = list()

        start = intervals[0].start
        end = intervals[0].end
        
        for this_interval in intervals[1:]:
            
            # overlap condition
            if this_interval.start <= end:
                end = max(end, this_interval.end)

            # non-overlap condition
            else:
                result.append(Interval(start, end))
                start = this_interval.start
                end = this_interval.end

        # add the last inverval
        result.append(Interval(start, end))

        return result
