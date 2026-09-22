#The FizzBuzz Classic (Number Classification)

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(str(n))
FizzBuzz(n)