class Vehicle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

    def speak(self):
        print(self.gas)

tim = Vehicle(100, 50, 'red')
tim.speak()
tim.gasLeft()
tim.fillUpTank()
tim.speak() 
