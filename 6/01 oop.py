## Object-Oriented Programming (OOP) in ython
# OOP allows us to create 'blueprints' that group functions and variables into a single object that represents something.


# For example, to represent a 'person' we might use the following dictionary
person = {
    "name": "Bob",
    "age": 21,
}

# to access the data we might do:
print(person["name"])
# the issue with dictionaries are that the keys and values are not guaranteed
# (person["age"] might not exist)

# we can use classes instead!
# classes act as the blue print for the object
class Person:
    # init is a SPECIAL method called the class constructor
    # its used to initialise that class attributes (self.something)
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    # allows for person.name
    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    # allows for updating person.name
    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    # custom print so print(person) = "Person: Bob (5 years old)"
    def __str__(self):
        return f"Person: {self._name} ({self._age} years old)"

    # you can also define custom functiosn
    def introduce(self):
        print(f"Hello my name is {self._name} and I am {self._age}")


# to use an object ObjectName(arguments for __init__ excluding self):
person_variable_1 = Person(
    "Bob", 21
)  # creates an INSTANCE of Person and stores it in the variable
print(person_variable_1.name)  # @property
person_variable_1.name = "New Name"  # @name.setter
print(person_variable_1)  # __str__

person_variable_2 = Person("Person 2", 50)
total_age = person_variable_1.age + person_variable_2.age
person_variable_2.introduce()  # use the function

# Inheritance and Polymorphism
# inheritance allows classes to be 'subclasses'
# for example, a person can be a teacher or student but both are still persons
# this means that both teachers and students have 'name' and 'age' but a teacher can have a 'university' and the student has a 'favourite_teacher'

# when you define the the sub class, you write
# class Subclass(Class):
class Student(Person):
    def __init__(self, name, age, favourite_teacher):
        super().__init__(name, age)  # call init of main class
        self._favourite_teacher = favourite_teacher

    # * polymorphism allows different classes to 'override' functions of the base class
    def introduce(self):
        print(
            f"Hello my name is {self._name} and I am {self._age}, my favourite teacher's name is {self._favourite_teacher}"
        )


student = Student("Student name", 12, "Teacher name")
student.introduce()

# * Excercise
# Create a class called 'Animal' with the following attributes: 'name', 'weight'
# Include the method / function 'make_sound' that should print "Hi I don't know what to say"
# Create the subclass called 'Cat' with the extra attribute: 'has_short_legs'
# Create the subclasses called 'Dog' with the extra attribute: 'is_hairy'
# Both subclasses should override the 'make_sound' method with the relevant sounds
# Update the __str__ function for both classes so they print "Hi I am a Dog, and my name is {}"
# Create an instance of a dog: "Dog1", 50, True (is_hairy), name the variable dog1
# Create an instance of a dog: "Dog2", 25, False (is_hairy), name the variable dog2
# Create an instance of a cat: "Meower1", 12, False (has_short_legs), name the variable kitty1
# print the ouptut of __str__ for dog1
