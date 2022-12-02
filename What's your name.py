def print_full_name(first, last):
    s1="Hello"
    s2="!"
    s3="You just delved into python"
    print(s1,first,last+s2,s3)
if __name__ == '__main__':
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    print_full_name(first_name, last_name)
