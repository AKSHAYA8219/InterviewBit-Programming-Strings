# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        words=A.split()
        if(len(words)==0):
            return 0
        return len(words[-1])
