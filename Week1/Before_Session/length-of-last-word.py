class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        counter = 0
        last_counter = 0
        has_word = False
        for c in A:
            if c == " ":
                if has_word == True:
                    last_counter = counter
                counter = 0
                has_word = False
            else:
                has_word = True
                counter += 1
                
        # Indicate that string finish with word                
        if has_word == True:
            return counter
        return last_counter
