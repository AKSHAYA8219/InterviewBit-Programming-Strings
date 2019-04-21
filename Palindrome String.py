# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        end = len(A) - 1
        start = 0
        if not A:
            return 1
        while start<end:
            if A[start].isalnum() and A[end].isalnum():
                ast = A[start].lower()
                aen = A[end].lower()
                if ast != aen:
                    return 0
                else:
                    start+=1
                    end-=1
            elif not A[start].isalnum():
                start+=1
            elif not A[end].isalnum():
                end-=1
            
        return 1
