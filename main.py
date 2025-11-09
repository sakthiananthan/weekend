# from calc import*

# print("welcome to calculator")

# # while True:
# i=0
# while i <3:
#     i+=1
#     print("you can perform following opration")
#     print("1.Addition\n2.Subtract\n3.Multipication\n4.division")
#     choice=input("Enter your choice [1,2,3,4] : ")
#     if choice in ["1","2","3","4"]:
#         num1=int(input("Enter first number: "))
#         num2=int(input("Enter Second number: "))
#         if choice == "1":
#             print(f"The number {num1} and {num2} is {add(num1,num2)}")
#         elif choice == "2":
#             print(f"The number {num1} and {num2} is {sub(num1,num2)}")
            
#         elif choice == "3":
#             print(f"The number {num1} and {num2} is {mul(num1,num2)}")
            
#         elif choice == "4":
#             result=div(num1,num2)
#             print(f"ans: {result[0]}")
#             print(f"q: {result[1]}")
#             print(f"r: {result[2]}")

#     else:
#         print("Invalide choice")
#     cont=input("Do you want to continue (y/n): ")
#     if not cont == "y":
#         print("Closing")
#         break
# print("Thank for using us")

# def validate_input(test,type):
#     return isinstance(test,type)

def validate_numeric(inp):
    for i in inp:
        if not i.isnumeric():
            return False
    return True

def validate_alpha(inp):
    for i in inp:
        if not i.isalpha():
            return False
    return True

num_flag=False
alpha_flag=False    
        
while True:
    if not num_flag:
        VAR_1=input("Enter var 1: ")
        VAR_2=input("Enter var 2: ")
    if not alpha_flag:
        VAR_3=input("Enter var 3: ")
        VAR_4=input("Enter var 4: ")
    if not validate_numeric([VAR_1,VAR_2]):
        print("validate_numeric is failed")
        print("asking for inputs again...")
    else:
        print("validate numeric passed...")
        num_flag=True
        print(num_flag)
        
    if not validate_alpha([VAR_3,VAR_4]):
        print("validate_alpha is failed")
        print("asking for inputs again...")
        continue
    else:
        print("validate alpha passed...")
        alpha_flag=True
        print(alpha_flag)
    
    print(f"Entered values: {VAR_1},{VAR_2}")
    if not (input("shall I continue(y/n): ")=="y"):
        print("asking for inputs again...")
    else:
        break

