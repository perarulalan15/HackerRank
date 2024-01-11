def welcome_pattern(N, M):
    pattern = []
    for i in range(1, N, 2):
        row = ".|." * i
        pattern.append(row.center(M, "-"))
    
    welcome_line = "WELCOME".center(M, "-")
    pattern.append(welcome_line)
    
    for i in range(N-2, 0, -2):
        row = ".|." * i
        pattern.append(row.center(M, "-"))

    for line in pattern:
        print(line)

input_values = input().split()
N, M = map(int, input_values)

        
welcome_pattern(N, M)
