from itertools import combinations
s,p=input("Enter string:").split()
result=list(combinations(s,int(p)))
final=(sorted(result))
for final in final:
    print("".join(final))