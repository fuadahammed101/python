# #Find the missing number from 1 to 10 without using a loop.

# a = [1,2,3,4,5,6,7,8,10]

# # n = 10

# # print(n * (n+1)//2 - sum(a))
# 1. Your list with TWO missing numbers (7 and 9 are missing)
a = [1, 2, 3, 4, 5, 6, 8, 10]
b = {5}
c = {4}
d = b - c
print(d)
# 2. Generate what the perfect list SHOULD look like using range()
# (Remember, range(1, 11) generates numbers from 1 to 10)
perfect_set = set(range(1, 11))
print(perfect_set)
# 3. Convert your incomplete list into a set
actual_set = set(a)
print(actual_set)
# 4. Subtract the sets! Python instantly finds the elements unique to perfect_set
missing_numbers = perfect_set - actual_set
print(missing_numbers)
# 5. Convert it back to a list to see the output cleanly
#print("The missing numbers are:", list(missing_numbers))
