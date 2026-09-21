from num2words import num2words
#print number from 0 to N
n = int(input("Enter the number: "))
print("\nRange 0 to n+1: ")
for i in range(n+1): #print 0 to n
    print(i, end=" ")
print("\n") #for creating newline and to avoid % form output


#print 0 to n-1
print("Range 0 to n-1: ") # keeping this outside the for loop
for i in range(n): #print 0 to n-1
    print(i, end=" ")
print("\n\n")

 #print spacificly within the range
print("Range 1 to n+1: ") 
for i in range(3, 8): #print spacificly within the range
    print(i, end=" ")


#print odd numbers only
print("\nOdd values are: ")
for i in range(n+1):
    if i % 2 != 0: #print only odd numbers
        print(i, end=" ")

#print even numbers only
print("\nEven numbers are: ")
for i in range(1,n+1):
    if i % 2 == 0:
        print(i, end=" ")


#spacific gap
print("\nThe n+ 2 values are: ")
for i in range(0,n+1, 1): #(start, stop, step)*****
    print(i, end=" ")

#print in reserse
print("\nReserse values are: ")
for i in range(n,-1,-1):
    print(i,end=" ")


