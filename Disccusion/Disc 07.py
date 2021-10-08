class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, staff):
        self.name = name  # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1

#Questions 1.1 solutions:

# callahan = Professor("Callahan")
# elle = Student("Elle", callahan)
# elle.visit_office_hours(callahan)
# elle.visit_office_hours(Professor("Paulette"))
# print(elle.understanding)
# print([name for name in callahan.students])
# x = Student("Vivian", Professor("Stromwell")).name
# print(x)
# print([name for name in callahan.students])


#Questions 1.2 solutions:
class MinList(object):
    def __init__(self):
        self.items = []
        self.size = 0
    def append(self,item):
        self.items.append((item))
        self.size +=1
    def pop(self):
        item = min(self.items)
        self.items.remove(item)
        self.size -=1
        return item

m = MinList()
m.append(4)
m.append(2)
print(m.size)

m = MinList()
m.append(4)
m.append(1)
m.append(5)
print(m.pop())
print(m.size)


#Questions 1.3 solutions:
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name. """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, which is a dictionary that associates client names with
    client objects. """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to. """
        return self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them to the clients instance attribute. """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is used for addressing emails to the client), server (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received). """

    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client. """
        return self.server.send(Email(msg,self.name,recipient_name,))


    def receive(self, email):
        """Take an email and add it to the inbox of this client. """
        self.inbox.append(email)


#Questions 2.1 solutions:
# class Dog():
#     def __init__(self, name, owner):
#         self.is_alive = True
#         self.name = name
#         self.owner = owner
#     def eat(self, thing):
#         print(self.name + " ate a " + str(thing) + "!")
#     def talk(self):
#         print(self.name + " says woof!")

# class Cat():
#     def __init__(self, name, owner, lives=9):
#         self.is_alive = True
#         self.name = name
#         self.owner = owner
#         self.lives = lives
#     def eat(self, thing):
#         print(self.name + " ate a " + str(thing) + "!")
#     def talk(self):
#         print(self.name + " says meow!")

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives
    def talk(self):
        print(self.name + " says meow!")
    def lose_life(self):
        if(self.lives>0):
            self.lives -=1
            return
        else:
            self.is_alive = False
            print("{0} has no more lives to lose".format(self.name))

# Cat('Thomas', 'Tammy').talk()

#Questions 2.2 solutions:
class NoisyCat(Cat):
    def talk(self):
        print(self.name + " says meow!")
        print(self.name + " says meow!")
    def __repr__(self):
        return ("NoisyCat({0}, {1})".format(self.name,self.owner))

print("************************")
NoisyCat('Magic', 'James').talk()

muffin = NoisyCat('Muffin', 'Catherine')
print(repr(muffin))
print(muffin)
