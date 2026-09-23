string = (input("Enter anything: "))

digits_only = ""
alphabet_only = ""
for char in string:
    if char.isdigit():
        digits_only += char
        
    elif char.isalpha():
        alphabet_only += char

print("Number: ",digits_only)
print("Alphabet: ",alphabet_only)



# if digits_only != "":
#     age = int(digits_only)


# if age >=18:
#     print("\nok")
# else:
#     print("not eligible")