n, arr = int(input()), list(map(int, input().split()))
print(all(x > 0 for x in arr))
