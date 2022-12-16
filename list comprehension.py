X=2
Y=2
Z=2
N=2
output = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print(output)