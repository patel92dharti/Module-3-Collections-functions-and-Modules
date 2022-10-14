#Write a Python function that checks whether a passed string is palindrome or not

def palindrome_f(String):
    Left=0
    Right=len(String)-1
    while Right>=Left:
        if not String[Left]==String[Right]:
            return False
        Left=Left+1
        Right=Right-1
    return True
print(palindrome_f(input("String:")))
