def find_pythagorean_triplet(sum: int) -> int:
    for a in range(1, sum//3):
        for b in range(a+1, (sum - a)//2 + 1):
            c = sum - a - b
            
            if a**2 + b**2 == c**2:
                return a*b*c
            
SUM=1000
print(find_pythagorean_triplet(SUM))