class Cal():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def plus(self):
            result = self.num1 + self.num2
            return result
    def minus(self):
            result = self.num1 - self.num2
            return result
    def multiple(self):
            result = self.num1 * self.num2
            return result
    def divide(self):
            result = self.num1 / self.num2
            return result
calc = Cal(20,10)
print(calc.plus())