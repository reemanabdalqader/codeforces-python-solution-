//https://codeforces.com/group/MWSDmqGsZm/contest/223338/problem/E
import math
n = int(input ()) 
discriminant =1+(4*n*2)
sqrt_discriminant =math.sqrt(discriminant )
ans =(sqrt_discriminant-1)/2
print (int (ans) )
