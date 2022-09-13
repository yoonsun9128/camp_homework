class Area():
    PIE = 3.14
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def square(self):
        result = self.num1 * self.num2
        return result
    def triangle(self):
        result = self.num1 * self.num2
        return result
    def circle(self):
        result = ((self.num1/2)**2)* 3.14 
        return result
a = Area(10,20)
print(a.square())
print(a.triangle())
print(a.circle())