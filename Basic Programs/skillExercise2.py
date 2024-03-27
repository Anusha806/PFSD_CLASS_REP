#Factorial of number1st

'''
n=int(input("Enter a Number: "))
if n==0:
    print("Wrong input")
else:
    factorial=1
    for i in range(1,n+1):
        factorial *= i
    print(factorial)


'''

#1st 7 multiples of 7 2nd one

'''
i=7
j=1
n=7
while(j<=n):
    print(i,"*",j,"=",i*j)
    j+=1

'''

#Right Angle Triangle 3rd one

'''
x=0
str1="******************"
for i in str1:
    x=x-1
    print(str1[0:x])

for i in str1:
     x = x+ 1
     print(str1[0:x])
     
'''
#Binary to decimal

def binary_divisible_by_five(sequence):
    binary_numbers = sequence.split(',')
    result_numbers = []

    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:
            result_numbers.append(binary_number)

    result_sequence = ','.join(result_numbers)
    return result_sequence


input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

# Process the input and print the result
output_sequence = binary_divisible_by_five(input_sequence)
print("Numbers divisible by 5:", output_sequence)


#Right Angle Triangle 3rd one
'''
a, b, c = map(float, input("Enter three sides of the triangle (space separated): ").split())
is_right_angle_triangle = sorted([a, b, c])[0]**2 + sorted([a, b, c])[1]**2 == sorted([a, b, c])[2]**2
print("It is a right-angled triangle." if is_right_angle_triangle else "It is not a right-angled triangle.")
'''