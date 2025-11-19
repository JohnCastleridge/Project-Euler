import time

DIGITS = 3

def is_palindrome(num: int) -> bool:
    string = str(num)
    return string == string[::-1] 

start_time = time.perf_counter()

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


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(palindrome)