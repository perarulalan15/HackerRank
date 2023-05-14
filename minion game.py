def minion_game(string):
    string=string.upper()
    kevin=stuart=0
    l=len(string)
    for i, j in enumerate(string):
        p=l-i
        if j in {"A","E","I","O","U"}:
            kevin += p
        else:
            stuart += p
    if kevin == stuart:
        print("Draw")
    else:
        print(*("Stuart",stuart) if stuart>kevin else ("Kevin",kevin))
if __name__ == '__main__':
    s = input("Enter string:")
    minion_game(s)
