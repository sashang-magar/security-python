def miller_rabin(n, a):
    # Step 1: Write n - 1 as 2^k * m
    k = 0
    m = n - 1
    while m % 2 == 0:
        m //= 2
        k += 1
    print(f"Step 1: {n}-1 = 2^{k} * {m}")

    # Step 2: Compute b0 = a^m mod n
    b = pow(a, m, n)
    print(f"Step 2: b0 = {a}^{m} mod {n} = {b}")

    if b == 1 or b == n - 1:
        print("Probably Prime (b0 = 1 or n-1)")
        return True  # probably prime

    # Step 3: Repeat squaring
    for i in range(1, k):
        b = pow(b, 2, n)
        print(f"b{i} = b{i-1}^2 mod {n} = {b}")
        if b == n - 1:
            print("Probably Prime")
            return True  # probably prime
        if b == 1:
            print("Composite (got 1 before seeing n-1)")
            return False  # definitely composite

    print("Composite (never saw n-1)")
    return False  # definitely composite


n = int(input("Enter the number to test for primality: "))
a = 2  # base

print(f"\nTesting if {n} is prime using base a = {a}")
is_probably_prime = miller_rabin(n, a)

if is_probably_prime:
    print(f"\nResult: {n} is probably prime.")
else:
    print(f"\nResult: {n} is composite.")