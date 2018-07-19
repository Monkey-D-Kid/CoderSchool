class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        list_of_subarray = []
        subarray = []
        sum = 0
        length = 0
        starting = -1

        for i in range(len(A)):
            if A[i] >= 0:
                sum += A[i]
                length += 1
                if starting == -1:
                    starting = i
                
            else:
                if length == 0:
                    continue
                subarray = [sum, length, starting]
                list_of_subarray.append(subarray)
                sum = 0
                length = 0
                starting = -1

        if length != 0:
            subarray = [sum, length, starting]
            list_of_subarray.append(subarray)
	#TODO: Do comparision before add it to parent list
        max_s = 0
        max_l = 0
        min_i = 0
        for s,l,i in list_of_subarray:
            if s > max_s:
                max_s = s
                min_i = i
                max_l = l
            elif s == max_s:
                if l > max_l:
                    max_l = l
                    min_i = i
                elif l == max_l:
                    if i < min_i:
                        min_i = i

        return A[min_i:min_i+max_l]
