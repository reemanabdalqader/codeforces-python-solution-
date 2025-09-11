#https://codeforces.com/problemset/problem/200/B
n =int (input ())
arr = list(map(int, input().split()))  # نقسم السطر على الفراغات ونحول لكل رقم صحيح
ans =sum(arr)
tot =ans/n
print (f"{tot:.12f}")
