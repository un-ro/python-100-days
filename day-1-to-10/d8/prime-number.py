# Day 8 Exercise: Prime Number

def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
