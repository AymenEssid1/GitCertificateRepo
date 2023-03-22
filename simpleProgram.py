def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# iterate through all numbers up to 1000 and print the prime ones
for i in range(2, 1001):
    if is_prime(i):
        print(i+1)


print("THIS PROGRAM DISPLAYS ALL PRIME NUMBERS UP TO 1000")
print("done")