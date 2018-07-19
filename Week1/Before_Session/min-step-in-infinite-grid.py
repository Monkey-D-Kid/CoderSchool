class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def countStep(self, x_source, y_source, x_target, y_target):
        x_distance = abs(x_target - x_source)
        y_distance = abs(y_target - y_source)
        return max(x_distance, y_distance)
        
    def coverPoints(self, A, B):
        step = 0
        if len(A) < 2:
            return 0
        for i in range(len(A)-1):
            step += self.countStep(A[i], B[i], A[i+1], B[i+1])
        return step
