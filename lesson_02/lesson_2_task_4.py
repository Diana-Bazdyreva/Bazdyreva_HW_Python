n = int(input("Введите число: "))


def fizz_buzz(n):
    for x in range(1, n + 1):
        if (x % 3) == 0 and (x % 5) == 0:
            print(f"{x} - FizzBuzz")
        elif x % 3 == 0:
            print(f"{x} - Fizz")
        elif x % 5 == 0:
            print(f"{x} - Buzz")
        else:
            print(x)


fizz_buzz(n)
