from itertools import permutations
s,p=input("Enter string:").split()
result=list(permutations(s,int(p)))
final=(sorted(result))
for final in final:
    print("".join(final))