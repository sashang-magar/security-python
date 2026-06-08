def gcd(a,b):
    while b != 0:
        a, b = b , a % b
    return a

num1  = int(input("Enter 1st number: "))    
num2  = int(input("Enter 2nd number: "))    

print('GCD: ', gcd(num1 , num2))