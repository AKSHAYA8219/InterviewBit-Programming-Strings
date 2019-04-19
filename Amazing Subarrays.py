# You are given a string S, and you have to find all the amazing substrings of S.
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vow=['a','e','i','o','u','A','E','I','O','U']
        l=len(A)
        count=0
        for i in range(l):
            if(A[i] in vow):
                count+=((l-i)%10003)
        return count%10003
