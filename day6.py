name = input("Enter your sweet name: ")
age = int(input("Enter your age: "))
print("hello",name,"you will be",age+5,"in 5 years")


a = int(input("Enter the first number: "))
b = int(input("Enter the secound number: "))
a,b = b, a
print("before swapping a=", a , "b=", b)
print("after swapping a=", b , "b=", a)


pi = 3.14
r = float(input("enter radius: "))
area = pi * r * r
print("The area of the circle is: ",area)

p = float(input("principle: "))
r = float(input("rate % :"))
t = float(input("Time (years): "))
SI = (p*r*t)/100
print("sample intrest is :",SI)

x = int(input("enter number : "))
y = int(input("enter number : "))
z = int(input("enter number : "))
maximum = max(x,y,z)
print("maximum amoung x,y,z is : ",maximum)
