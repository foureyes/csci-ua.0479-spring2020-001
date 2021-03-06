"""
If we want to create a class that's mostly the same as another class
... we can "extend" or "inherit" from that other class
"""
class Person:
    def __init__(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last
        # self.full_name = first + ' ' + last

    def __str__(self):
        return self.title + ' ' + self.last

    def full_name(self):
        return self.first + ' ' + self.last

    def say_greeting(self, greeting):
        return greeting + self.first


# to extend an existing class, put in the parens following the "child" class name
# a parent (or super) class will be the class that methods and attributes will be inherited from
# a child class (or a sub class) will be the class that gets the methods and attributes
class Student(Person):
    def __init__(self, title, first, last, netid):
        # when we call super, we get access to the super / parent class methods
        # use super when you're in the class
        super().__init__(title, first, last)
        self.netid = netid

    def full_name(self):
        return 'STUDENT ' + self.first + ' ' + self.last
    
    # this method is called only on student objects
    # person objects don't have this
    def do_homework(self):
        return 'done'

s = Student('Mr', 'Joe', 'Versoza', 'jjv222')
print(s)
print(s.netid)
print(s.say_greeting('hi'))
print(s.full_name())


















