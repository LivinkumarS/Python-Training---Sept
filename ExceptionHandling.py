# print("Step1")
# print("Step2")
# print("Step3")

# ans=int("hello")
# print(ans)

# print(5/0)
# print("Final Step!")

try:
    def getValue(a,b):
        return (a+b)/(a-b)
    num1=int(input("Num1:"))
    num2=int(input("Num2:"))
    print(getValue(num1,num2))
except ZeroDivisionError:
    print("Invalid inputs!")
except ValueError:
    print("Enter valid numbers!")
finally:
    print("Final step!")

