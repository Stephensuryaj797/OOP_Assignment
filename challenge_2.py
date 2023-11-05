class Calculator():
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        add=self.num1+self.num2
        return add
    
    def subtract(self):
        sub=self.num1-self.num2
        return sub
    
    def multiply(self):
        pro=self.num1*self.num2
        return pro
    
    def divide(self):
        div=self.num2/self.num1
        return div


obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()