def armstrong_num(n):
    if n < 0:
        return False

    original = n
    sum = 0
    k = len(str(n))

    while n > 0:
        digit = n % 10
        sum = sum + (digit ** k)
        n = n // 10

    if sum == original:
        return True
    else:
        return False
print("sum = ",sum)
print("Is the number an armstrong number? = ",armstrong_num(int(input("Enter your number: "))))