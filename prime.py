num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not prime.")
elif all(num % i for i in range(2, int(num ** 0.5) + 1)):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")