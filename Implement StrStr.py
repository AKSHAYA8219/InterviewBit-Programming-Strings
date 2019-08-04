'''
Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases. 

'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        la=len(A)
        lb=len(B)
        if(la==0 or lb==0):
            return -1
        for i in range(0,la-lb+1):
            if A[i]==B[0]:
                if A[i:i+len(B)]==B:
                        return i
        return -1
