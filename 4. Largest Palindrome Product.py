DIGITS = 3

def is_palindrome(num: int) -> bool:
    string = str(num)
    return string == string[::-1] 

palindrome = 0
stop = None
for i in range(int('9'*DIGITS), 0, -1):
    for j in range(i, 0, -1):
        prod=i*j

        if prod < palindrome:
            break

        if is_palindrome(prod):
            palindrome = max(palindrome, prod)
            stop = j
            break
    
    if i == stop:
        break

print(palindrome)