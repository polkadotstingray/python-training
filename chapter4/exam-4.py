f1 = "50"
f2 = "100"
print(max(int(f1),int(f2)))

n = 1021
def prime(n):
    prime = True
    for i in range(2, n//2):
        if n % i == 0:
            prime = False
            break
    return prime

print(prime(n))