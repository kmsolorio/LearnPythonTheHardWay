## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
  pass

## Dog is-a Animal
class Dog(Animal):
  
  def __init__(self, name):
    ## has-a
    self.name = name

## is-a Animal
class Cat(Animal):
  
  def __init__(self, name):
    ## has-a
    self.name = name

## is-a object
class Person(object):
  
  def __init__(self, name):
    ## has-a name
    self.name = name
    
    ## Person has-a pet of some kind
    self.pet = None

## is-a Person
class Employee(Person):
  
  def __init__(self, name, salary):
    ## is-a Person
    super(Employee, self).__init__(name)
    ## has-a salary
    self.salary = salary

## is-a object
class Fish(object):
  pass

## is-a Fish
class Salmon(Fish):
  pass

## is-a Fish
class Halibut(Fish):
  pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()