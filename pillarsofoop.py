# Inheritance
class Birds:
  def __init__(self):
    print('Bird Class')

  def whoIsThis(self):
    print('Its Bird !!')

  def swim(self):
    print('Swimming in Sky !!')

class Penguin(Birds):
  def __init__(self):
    super().__init__()

  def whoIsThis(self):
    print('Its Penguin')

  def run(self):
    print('Run Faster !!')

p=Penguin()
print(p.whoIsThis())
print(p.swim())
print(p.run())

#Polymorphism

class Animal:
  def name(self):
    pass
  def sleep(self):
    print('Animal Sleeping !!')
  def makeNoise(self):
    pass

class Dog(Animal):
  def name(self):
    print('I am a dog !!')
  def makeNoise(self):
    print('Wooof... !!')

class Cat(Animal):
  def name(self):
    print('I am a cat !!')
  def makeNoise(self):
    print('Meow... !!')

class Lion(Animal):
  def name(self):
    print('I am a Lion !!')
  def makeNoise(self):
    print('Roar... !!')

class ManyForms:
  def getName(self, animal):
    animal.name()
  def GotoSleep(self, animal):
    animal.sleep()
  def makeNoise(self, animal):
    animal.makeNoise()

test=ManyForms()
dog= Dog()
cat= Cat()
lion= Lion()

print(test.getName(dog))
print(test.GotoSleep(dog))

#Abstraction/Encapsulation

class Mobile:
  def __init__(self):
    self.__price=9000
    self.company='Nokia'

  def getPrice(self):
    print('Price of this mobile phone is : ', self.__price)

  def setPrice(self, price):
    self.__price=price

mob=Mobile()

print(mob.getPrice())

print(mob.setPrice(1000))
print(mob.getPrice())