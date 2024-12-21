# for i in range(3):
#     print("sudip")

# for i in range(5):
#     print("i")

# for i in range(1,11,1):
#     print("i")

# word="sudip"
# for i in word:
#     print(i)

# for i in range(10,4,-1):
#     print(i)

# a=-6
# b=6
# if a>0 and b>0:
#     print("both are true")
# else:
#     print("Any one is false")

# a=-90
# b=-6
# if a>0 or b>0:
#     print("any one is true")
# else:
#     print("both are false")

# x=1
# print(not x)
# y=0
# print(not y)

# a = input("enter the word 1:")
# b = input("enter the word 2:")
# if a !=b:
#     print(a,'and',b,'are different.')
# else:
#     print(a,'and',b,'are same.')

# a=4
# b=5
# if(a==1)!=(b==5):
#     print('hello')
# else:
#     print("hai")

# a=int(input("enter a number"))
# if a%2 !=0:
#     print(a,"is not even number.")
# else:
#     print("Even number")

height =float(input("enter your height in cm:"))
weight =float(input("enter your weight in kg:"))
BMI=weight/(height/100)**2
print("you BMI is",BMI)
if BMI <=18.4:
    print("you are underweight.")
elif BMI <=24.9:
     print("you are healthy.")
elif BMI <=29.9:
     print("you are over weight.")
elif BMI <=34.9:
     print("you are severly over weight.")
elif BMI <=39.9:
     print("you are obese.")
else:
    print("you are severely obese." )

