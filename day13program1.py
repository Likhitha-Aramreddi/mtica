def solveproblem(s):
    lst=s.split()
    return[len(i) for i in lst]
inp=input()
print(*solveproblem(inp))
