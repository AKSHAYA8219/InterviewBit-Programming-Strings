'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        s=[]
        result=""
        for i in range(0,B):
            s.append("")
        count=0
        while(count<len(A)):
            for i in range(0,B):
                if(count==len(A)):
                    break
                s[i]=s[i]+A[count]
                count+=1
            for i in range(B-2,0,-1):
                if(count==len(A)):
                    break
                s[i]=s[i]+A[count]
                count+=1
        for i in s:
            result+=i
        return result
