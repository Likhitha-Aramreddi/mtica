def interchange2and0(n):
    n=str(n)
    n=n.replace('2','.')
    n=n.replace('0','2')
    n=n.replace('.','0')
    return n
n=int(input())
print(interchange2and0(n))

