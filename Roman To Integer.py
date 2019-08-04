'''
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20
'''



class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(self, A):
	    result=0
	    dic={'M':0,'D':1,'C':2,'L':3,'X':4,'V':5,'I':6}
	    value={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
	    i=0
	    while(i<len(A)-1):
	        a=A[i]
	        b=A[i+1]
	        if(dic[a]<=dic[b]):
	            result+=value[a]
	            i+=1
	        else:
	            result+=value[b]-value[a]
	            i+=2
	    if(i==len(A)-1):
	        result+=value[A[i]]
	    return result
