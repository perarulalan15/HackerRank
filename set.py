n=int(input("Enter no.of.set:"))
s=set(map(int, input("Enter set:").split()[:n])) 
N=int(input("Enter no.of.commands:"))
for i in range(N):
    c=list(input("Enter commands:").split())
    if c[0]=='pop':
        s.pop()
    elif c[0]=='remove':
        s.remove(int(c[1]))
    elif c[0]=='discard':
        s.discard(int(c[1]))
print(sum(s))