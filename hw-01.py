def valueInRange(nums, start, end):
    for num in nums:
        if start <= num <= end:
            yield num


def oddNumbers(nums):
    for num in nums:
        if num % 2 != 0:
            yield num


def multiples(nums, multiple):
    for num in nums:
        if num % multiple == 0:
            yield num


def palindromes(nums):
    for num in nums:
        if str(num) == str(num)[::-1]:
            yield num


nums = list(map(int, input("Пропишите числа через пробел: ").split()))
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in valueInRange(nums, start, end):
    print(num)

for num in oddNumbers(nums):
    print(num)

multiple = int(input("Введите число для проверки кратности: "))

for num in multiples(nums, multiple):
    print(num)

for num in palindromes(nums):
    print(num)