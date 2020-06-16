'''
There are N students standing in a row and numbered 1 through N from left to right. You are given a string S with length N, where for
each valid i, the i-th character of S is 'x' if the i-th student is a girl or 'y' if this student is a boy. Students standing next to
each other in the row are friends.

The students are asked to form pairs for a dance competition. Each pair must consist of a boy and a girl. Two students can only form
a pair if they are friends. Each student can only be part of at most one pair. What is the maximum number of pairs that can be formed?

Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single string S.

Output:
For each test case, print a single line containing one integer ― the maximum number of pairs.
'''


for _ in range(int(input())):
    arr = input()
    count = 0
    i = 0
    while i < len(arr)-1:
        if (arr[i] =='x' and arr[i+1] == 'y') or (arr[i]=='y' and arr[i+1]=='x'):
             count+=1
             i+=1
        i+=1
    print (count)
