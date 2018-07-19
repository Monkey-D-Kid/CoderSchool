class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        import re
        regex = re.compile('[^a-zA-Z0-9]')
        alphanumetric = regex.sub('', A)
        lower_case = alphanumetric.lower()
        for i in range(len(lower_case)/2):
            if lower_case[i] != lower_case[-1-i]:
                return 0
        return 1
