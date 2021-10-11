# Animal is-a object
class Animal(object):
    pass


# Dog is-a class is-a Animal is-a object
class Dog(Animal):
    def __init__(self, name):
        # takes name a parameter
        self.name = name


# Cat is-a class is-a Animal is-a object
class Cat(Animal):
    def __init__(self, name):
        # takes name as a parameter
        self.name = name


# Person is-a object
class Person(object):
    def __init__(self, name):
        # takes parameter name
        self.name = name
        self.pet = None


# Employee is-a person is-a object
class Employee(Person):
    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        # add salary attribute to person
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish is-s object
class Salmon(Fish):
    pass


# Halibut is-a Fish is-a object
class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rover")


# satan is-a cat
satan = Cat("Satan")


# marry is-a person
mary = Person("Marry")


# mary has-a pet , set pet attribute to satan
mary.pet = satan


# frank is-a Employee is-a object
frank = Employee("Frank", 10000)


# frank has-a pet , set pet attribute to rover
frank.pet = rover


# flipper is-a Fish is-a Animal is-a objcet
flipper = Fish()


# crouse is-a Salmon is-a Fish is-a Animal is-a object
crouse = Salmon()


# harry is-a Halibut is-a Fish is-a Animal is-a object
harry = Halibut()



