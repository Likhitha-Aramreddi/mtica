ans=[]
for i in range(1,1001):
    if i%8==0:
      ans.append(i)
print(ans)

ans=[i for i in range(1,10001)if i%8==0]
print(ans)
