'''
task: https://www.interviewbit.com/problems/reorder-data-in-log-files/

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

- The letter-logs come before all digit-logs.
- The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
- The digit-logs maintain their relative ordering.

Return the final order of the logs.

Problem Constraints
1 <= logs.length <= 1000
3 <= logs[i].length <= 1000
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.

Input Format
The first argument is a string array A where each element is a log.

Output Format
Return the string array A after making the changes.

-------------------------------------------------------------------------

Example Input

Input 1:
>>> A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
["let1-art-can","let3-art-zero","let2-own-kit-dig","dig1-8-1-5-1","dig2-3-6"]

Explanation 1:
The letter-log contents are all different, so their ordering is "art-can", "art-zero", "own-kit-dig".
The digit-logs have a relative order of "dig1-8-1-5-1", "dig2-3-6".

Input 2:
>>> A = ["a1-9-2-3-1","g1-act-car","zo4-4-7","ab1-off-key-dog","a8-act-zoo"]
["g1-act-car", "a8-act-zoo", "ab1-off-key-dog", "a1-9-2-3-1", "zo4-4-7"]

Explanation 2:
The array has been sorted restricted to the conditions given.
'''

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def reorderLogs(self, A):
        
        sorted_logs = list()
        raw_numerical_logs = list()
        raw_alphabetical_logs = list()

        # separate the numerical from the alphabetical logs
        for log_message in A:

            log_elements = log_message.split('-')
            log_identifier = log_elements[0]
            first_log_element = log_elements[1]

            # this is a nemerical log message
            if first_log_element.isdigit():
                raw_numerical_logs.append(log_message)

            # this is a alphabetical log message
            else:
                raw_alphabetical_logs.append(log_message)

        sorted_alphabetical_logs = list()

        # sort the alphabetical logs by their CONTENTS
        for alphabetical_log in raw_alphabetical_logs:

            # strip the string
            first_delimiter_location = alphabetical_log.find('-')
            sripped_alphabetical_log = alphabetical_log[first_delimiter_location:]

            entry = {
                'alphabetical_log': alphabetical_log,
                'sripped_alphabetical_log': sripped_alphabetical_log
            }

            sorted_alphabetical_logs.append(entry)

        # now, everything is sorted based on the contents of the alphabetic string
        sorted_alphabetical_logs.sort(key=lambda x: x['sripped_alphabetical_log'])

        # replace the array with the full length log strings
        sorted_alphabetical_logs = [d['alphabetical_log'] for d in sorted_alphabetical_logs]

        # add the full string to the sorted_logs
        for alphabetical_log in sorted_alphabetical_logs:
            sorted_logs.append(alphabetical_log)

        for numerical_log in raw_numerical_logs:
            sorted_logs.append(numerical_log)

        return sorted_logs

s = Solution()

result = s.reorderLogs(A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"])
expected = ["let1-art-can","let3-art-zero","let2-own-kit-dig","dig1-8-1-5-1","dig2-3-6"]
print(result == expected)

result = s.reorderLogs(A = ["a1-9-2-3-1","g1-act-car","zo4-4-7","ab1-off-key-dog","a8-act-zoo"])
expected = ["g1-act-car", "a8-act-zoo", "ab1-off-key-dog", "a1-9-2-3-1", "zo4-4-7"]
print(result == expected)

