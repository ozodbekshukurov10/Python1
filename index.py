son = int(input('sondi kriting: '))

class person:
    def __init__(self, number):
        self.number = number


    def greet(self):
        return self.number **2
    
    def welcome(self):
        return self.number ** 3
    
    def ildiz(self):
        return self.number ** 0.5
    

p1 = person(son)

print('kvadrat')
print(p1.greet())
print('kub')
print(p1.welcome())
print('ildiz')
print(p1.ildiz())
        