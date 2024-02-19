# Calculator with Class and Methods

class Calc:

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2
    
    def extraction(self):
        if self.num2 == 0:
            return 0
        return self.num1 - self.num2

num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))

Calc1 = Calc(num1,num2)

selection = input("Add (1), Multiply (2), Div (3), Ext (4), Please Select Your Operation: ")
match selection:
    case "1":
        print(f"Result = {Calc1.add()}")
    case "2":
        print(f"Result = {Calc1.multiply()}")
    case "3":
        print(f"Result = {Calc1.division()}")
    case "4":
        print(f"Result = {Calc1.extraction()}")
    case _:
        print("Entered Wrong Operation.")