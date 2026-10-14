a = 2
b = 9
print(a + b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)



x = 10
print(x>5)
print(x==10)

age = 18
print(age > 15 and age < 20)


#control statement
num = int(input("enter a numer : "))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

marks = int(input("Enter a marks : "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("fail")            


#loop

for i in range(1, 6):
    print(i)    


x = 1
while x <= 5:
    print(x)
    x += 1    


num = int(input("enter the number :"))
for i in range (1 , n+1):
  if i % 2 == 0:
     print("even numbers are :",i)


num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, 'x' , i,'=',num * i)
    



for i in range(1, 11):
    print(i)

num = input("Enter the original number: ")
reverse = num[::-1]
print("The reversed number is:", reverse)

while True:
    print("--MENU DRIVEN--")
    print("1.even numver")
    print("prime number")
    print("exit")

    choice = int(input("enter your choice (1,2,3) : "))

    if choice == 1 :
        num = int(input("enter a number:"))
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

    elif choice == 2:
        num = int(input("enter a number:"))
        if num <= 0:
            print("not prime")
        else:
            is_prime = True
            for i in range(2,num):
                if num % i == 0:
                    is_prime = False
                    break

                if is_prime == True:
                    print("Prime number")
                else:
                    print("not prime")

    elif choice == 3:
        print("exiting the program.....") 
        break

    else:
        print("invalid choice-----* *-------")  
