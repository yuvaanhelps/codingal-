def power(base, exp):
    result = 1

    while exp > 0:
        if exp % 2 == 1:
            result *= base

        base *= base
        exp //= 2

    return result


num = int(input("Enter number: "))
n = int(input("Enter power: "))

print(power(num, n))