#program1(Power)

''''
n=int(input("Enter a Number"))
if n==0:
    print("Wrong Input")
else:
    for i in range (n,n+1):
        val = n*(n*1)
        print(val)
'''

#program2(Print String increasing )
'''''
x=0
str1="ThisismyCountryIndia"
for i in str1:
    x=x-1
    print(str1[0:x])
for i in str1:
    x=x+1
    print(str1[0:x])

'''
#program3(pattern)

'''
# Program for printing "*" according to the given input

n=int(input("Enter number of astriks you need:")) 
x=n 
for i in range (n):     
        print("*"*x) 
        x=x-1 
x=1 
for i in range (n): 
        print("*"*x) 
        x=x+1
'''

#program4(binary , decimal convertor)
'''
a1="1010"
a2=int(format(int(a1,2),'d'))
print(a2)

a3=1045
a4=format(a3,'x')
print(a4)

'''


#LAB EXCERCISE 1

#Calculate Average

'''
a=(10,20,30,40,50,60,70,80,90,100)
c=sum(a)/len(a)
print(c)
'''

#Print type
'''
a=input("Enter a value :")
print(type(a))
b=int(input("Enter b value :"))
print(type(b))
'''


#add complex,float,int values

'''
a=complex(input("Enter a complex value :"))
b=complex(input("Enter another complex value :"))
c=a+b
print(c)

m=float(input("Enter a float value :"))
n=float(input("Enter another float value :"))
o=m+n
print(o)

x=int(input("Enter a int value :"))
y=int(input("Enter another int value :"))
z=x+y
print(z)

'''

#convert int to float

'''
n=int(input("Enter an integer value"))
print(float(n))

'''

#addition of str and int


string = "123"
number = int(string)

print(f"Original string: {number}")
print(f"After conversion to integer: {number}")




