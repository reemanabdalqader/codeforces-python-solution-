#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/H
t=int( input())
for i in range(t):
    s=input().strip()
    test =False 
    n=len(s)
    for i in range(n-2):
        str1 =s[i:i+3]
        if str1 =="010"or str1=='101':
            test =True 
            break 
    if test :
        print ("Good")   
    else :
        print ("Bad") 
