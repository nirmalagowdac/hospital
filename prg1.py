class Calculater:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def addition (self):
        result = self.x + self.y
        print (result)
    def difference (self):
        result = self.x - self.y
        print (result)
    def multiplication (self):
        result = self.x * self.y
        print (result)
    def division (self):
        result = self.x / self.y
        print (result)
    def reminder (self):
        result = self.x % self.y
        print (result)
    def quotient (self):
        result = self.x // self.y
        print (result)
    def power (self):
        result = self.x ** self.y
        print (result)
c=calculater(10,20)
c.addition
c.difference
c.multiplication
c.division
c.remaindr
c.quotient
c.power
