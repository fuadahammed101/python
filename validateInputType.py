age = (input("Enter your age: "))

digits_only = ""
for char in age:
    if char.isdigit():
        digits_only += char
        print(char,end="")

if digits_only != "":
    age = int(digits_only)


if age >=18:
    print("\nok")
else:
    print("not eligible")