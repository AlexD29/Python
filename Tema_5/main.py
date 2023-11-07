import math

# 1
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

print("Ex. 1:")
circle = Circle(5)
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

triangle = Triangle(3, 4, 5)
print(f"Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")


#2
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Exceeded overdraft limit")

print("\nEx. 2:")
savings_account = SavingsAccount("SA123", 1000, 0.02)
savings_account.deposit(500)
savings_account.withdraw(200)
interest = savings_account.calculate_interest()

print(f"Savings Account - Account Number: {savings_account.account_number}, Balance: {savings_account.balance}, Interest: {interest}")

checking_account = CheckingAccount("CA456", 2000, 100)
checking_account.deposit(300)
checking_account.withdraw(2500)

print(f"Checking Account - Account Number: {checking_account.account_number}, Balance: {checking_account.balance}")


#3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def calculate_mileage(self):
        # Placeholder method for calculating mileage for cars
        # You can implement your own calculation logic here
        return 30  # Example: assuming 30 miles per gallon

class Motorcycle(Vehicle):
    def calculate_mileage(self):
        # Placeholder method for calculating mileage for motorcycles
        # You can implement your own calculation logic here
        return 50  # Example: assuming 50 miles per gallon

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity

print("\nEx. 3:")
car = Car("Toyota", "Camry", 2022)
car_mileage = car.calculate_mileage()

motorcycle = Motorcycle("Honda", "CBR600RR", 2022)
motorcycle_mileage = motorcycle.calculate_mileage()

truck = Truck("Ford", "F-150", 2022, 10000)
towing_capacity = truck.calculate_towing_capacity()

print(f"Car - Make: {car.make}, Model: {car.model}, Year: {car.year}, Mileage: {car_mileage} mpg")
print(f"Motorcycle - Make: {motorcycle.make}, Model: {motorcycle.model}, Year: {motorcycle.year}, Mileage: {motorcycle_mileage} mpg")
print(f"Truck - Make: {truck.make}, Model: {truck.model}, Year: {truck.year}, Towing Capacity: {towing_capacity} lbs")


#4
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def assign_task(self, task):
        print(f"Manager {self.name} assigns task: {task}")

class Engineer(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def code(self):
        print(f"Engineer {self.name} is coding")

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, commission_rate):
        super().__init__(name, employee_id)
        self.salary = salary
        self.commission_rate = commission_rate

    def make_sale(self, amount):
        commission = amount * self.commission_rate
        print(f"Salesperson {self.name} made a sale of {amount}. Commission: {commission}")

print("\nEx. 4:")
manager = Manager("John Doe", 1001, 80000)
manager.assign_task("Prepare quarterly report")

engineer = Engineer("Jane Smith", 1002, 70000)
engineer.code()

salesperson = Salesperson("Bob Johnson", 1003, 60000, 0.1)
salesperson.make_sale(10000)


#5
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"The {self.name} gives birth to live young")

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(f"The {self.name} is flying")

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def swim(self):
        print(f"The {self.name} is swimming in {self.water_type} water")

print("\nEx. 5:")
mammal = Mammal("Dog", 5, "Brown")
mammal.give_birth()

bird = Bird("Eagle", 3, 6.2)
bird.fly()

fish = Fish("Salmon", 2, "Fresh")
fish.swim()


#6
class LibraryItem:
    def __init__(self, title, author, item_id, checked_out=False):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = checked_out

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is already in the library."

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nItem ID: {self.item_id}\nChecked Out: {self.checked_out}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages, checked_out=False):
        super().__init__(title, author, item_id, checked_out)
        self.num_pages = num_pages

    def display_info(self):
        return f"{super().display_info()}\nNumber of Pages: {self.num_pages}"

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration, checked_out=False):
        super().__init__(title, director, item_id, checked_out)
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}\nDuration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, item_id, checked_out=False):
        super().__init__(title, "N/A", item_id, checked_out)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}\nIssue Number: {self.issue_number}"

print("\nEx. 6:")
book = Book("The Catcher in the Rye", "J.D. Salinger", 101, 234)
dvd = DVD("Inception", "Christopher Nolan", 201, 148)
magazine = Magazine("National Geographic", 315, 301)

print(book.display_info())
print(dvd.display_info())
print(magazine.display_info())

print(book.check_out())
print(dvd.check_out())
print(magazine.check_out())

print(book.return_item())
print(dvd.return_item())
print(magazine.return_item())
