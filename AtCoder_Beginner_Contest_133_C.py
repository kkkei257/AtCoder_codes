// https://atcoder.jp/contests/abc133/tasks/abc133_c

l,r = input().split()
l = int(l)
r = int(r)
N = int(2019)
  
ans = N
count = 0
right = min(l + N, r)
for i in range(l,right):
  for j in range(i+1,right+1):
    ans = min(ans, (i * j) % N)
    
print(ans)
