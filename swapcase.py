def swap_case(s):
    result=''
    for i in s:
        if (i.isupper())==True:
            result +=(i.lower())
        elif (i.islower())== True:
            result +=(i.upper())
        elif (i.isspace())==True:
            result += i
        elif i=='.'or'!'or'#':
            result += i
    return result
if __name__=='__main__':
    s=input("Enter string:")
    result=swap_case(s)
    print(result)

