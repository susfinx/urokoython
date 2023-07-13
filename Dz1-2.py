def check_prime(num):
    if num <= 1 or num > 100000:
        return "Число должно быть больше 1 и не превышать 100000."
    elif num == 2:
        return "Число является простым."
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return "Число является составным."
        return "Число является простым."

num = int(input("Введите число: "))
result = check_prime(num)
print(result)
