n = int(input("Enter no.of.scores:"))
arr = map(int, input("Enter score").split())
print(sorted(set(arr), reverse=True)[1])
