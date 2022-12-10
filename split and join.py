def split_and_join(line):
    result=line
    result=result.split(" ")
    result="-".join(result)
    return result
if __name__ == '__main__':
    line = input("Enter line:")
    result = split_and_join(line)
    print(result)
