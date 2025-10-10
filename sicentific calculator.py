import math
print("==================welcome to scientific calculator==================")
while True:
 try:
     mode=int(input("Enter the operation you want:\nFor addition press 1\nFor subtraction press 2\nFor multiplication press 3\nFor division press 4\nFor trigonometry press 5\nFor power operation press 6\nFor exit press 0\n"))
     match mode :
        case 1:
         operator = 0
         count = int(input("How many number are you entering "))
         for numbers in range(count):
          num = float(input("Enter the number "))
          operator+=num
         print(f"result = {operator} ")     
        case 2:
         count = int(input("How many number are you entering "))
         first_num = float(input("Enter the number "))
         for numbers in range(count-1):
          num = float(input("Enter the number "))
          first_num-=num
         print(f"result = {first_num} ")
        case 3:
         operator = 1
         count = int(input("How many number are you entering "))
         for numbers in range(count):
          num = float(input("Enter the number "))
          operator= operator * num
         print(f"result = {operator} ")          
        case 4:
         count = int(input("How many number are you entering "))
         first_num = float(input("Enter the number "))
         for numbers in range(count-1):
          num = float(input("Enter the number "))
          first_num/=num
         print(f"result = {first_num} ")     
        case 5:
          try :
           mode_1=int(input("For sin press 1\t\t For cos press 2\t For tan press 3\t For sinh press 4\t For cosh press 5\t For tanh press 6 "))   
           match mode_1 :
              case 1:
               deg=int(input("enter the angle in degree "))
               rad=math.radians(deg)
               print(f"result = {math.sin(rad)}")
              case 2:
               deg=int(input("enter the angle in degree "))
               rad=math.radians(deg)
               print(f"result = {math.cos(rad)}")
              case 3:
               deg=int(input("enter the angle in degree "))
               rad=math.radians(deg)
               print(f"result = {math.tan(rad)}")
              case 4:
               deg=int(input("enter the angle in degree "))
               rad=math.radians(deg)
               print(f"result = {math.sinh(rad)}")
              case 5:
               deg=int(input("enter the angle in degree "))
               rad=math.radians(deg)
               print(f"result = {math.cosh(rad)}")
              case 6:
               deg=int(input("enter the angle in degree "))
               rad=math.radians(deg)
               print(f"result = {math.tanh(rad)}")
          except ValueError:
              print("invalid operation please enter the number of the operation you want")                                            
        case 0:
         print("See you soon amigo goodbye :)")
         break
        case 6:
         base = int(input("Enter the base "))
         power = int(input("Enter the base "))
         result=base**power
         print(f"result = {result} ")
        case _:
          print("invalid operation please enter the operation you want\a")
 except ValueError:
     print("invalid operation please enter the number operation you want\a")
 print("\n")