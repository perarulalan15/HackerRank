N = int(input("Enter number:"))
alist=[]
for i in range(N):
    inp=input(("Enter operation:")).split()
    if inp[0]=="insert":
        alist.insert(int(inp[1]),int(inp[2]))
    elif inp[0]=="print":
        print(alist)
    elif inp[0]=="pop":
        alist.pop()
    elif inp[0]=="remove":
        alist.remove(int(inp[1]))
    elif inp[0]=="append":
        alist.append(int(inp[1]))
    elif inp[0]=="sort":
        alist.sort()
    elif inp[0]=="reverse":
        alist.reverse()
    else:
        break