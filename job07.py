list = list(range(1, 101, 1))
for nombre in list:
    if nombre % 3 == 0 and nombre % 5 != 0:
        print("Fizz")
    elif nombre % 5 == 0 and nombre % 3 != 0:
        print("Buzz")
    elif nombre % 5 == 0 and nombre % 3 == 0:
        print("FizzBuzz")
    else:
        print(nombre)
