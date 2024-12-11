def palindrome_check(s):
    if(s==s[::-1]):
        return True
    return False


s="madam"
s1="amaan"

print(palindrome_check(s))
print(palindrome_check(s1))