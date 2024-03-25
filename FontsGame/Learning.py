import pygame as pg
import math
import concurrent.futures
# Two of the many modules for accessing the internet and processing internet protocols
from urllib.request import urlopen  # Used for retrieving data from URLs
import threading
import time
import webbrowser

begin = time.perf_counter()
###################################################################################################################################################
pg.init()
a = 5
pos = (0, 0)
# Quick way to alter coordinates
pos += pg.math.Vector2(100, 100)
print(pos)


###################################################################################################################################################
# Function with arbitrary amount of parameters
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("Mercury", "Venus", "Earth", sep=" --> "))
###################################################################################################################################################
"""squares = []
   for x in range(10):
       squares.append(x**2)
is the same thing as:
squares = list(map(lambda x: x**2, range(10)))
or:
"""
squares = [x ** 2 for x in range(10)]
print(squares)

print(help(pg))  # Prints an extensive manual page created from the module's docstrings
print(dir(pg))  # Prints defined names of module

print(
    f'The value of pi is approximately {math.pi:.5f}.')  # The 5f rounds the number to 5 decimal places, and f stands for float.


###################################################################################################################################################
# Inheritance
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # Multiple inheritance is also possible, just add more parameters
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
###################################################################################################################################################
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()  # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())  # Remove trailing newline


###################################################################################################################################################
def do_something(n):
    time.sleep(n)


def do_something2(x):
    time.sleep(2 * x)


start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:  # Threading module
    result = executor.submit(do_something, 1)
    result2 = executor.submit(do_something2, 1)
    print(result, result2)

finish = time.perf_counter()
print(f"Threading finished in {round(finish - start, 2)} seconds")  # The threading took 2 seconds instead of 3
print(f"Code finished in {round(finish - begin, 2)} seconds")
###################################################################################################################################################
threading_class_start = time.perf_counter()


class ThreadingClass(threading.Thread):  # This can of course be put at the top of the file to not have to wait for everything else to complete
    def __init__(self, y):
        threading.Thread.__init__(self)
        self.y = y

    def run(self):
        time.sleep(self.y)


background = ThreadingClass(1)  # Runs only the function names run ThreadingClass, it must be named run
background.start()
print('The main program continues to run in foreground.')
# Use background.join() when you need task to finish
background.join()  # Wait for the background task to finish
threading_class_end = time.perf_counter()
print(f"Threading class took {round(threading_class_end - threading_class_start, 2)} seconds")
###################################################################################################################################################
# Prints the memory address of controller object for the browser type used
print(int(str(webbrowser.get(using=None))[-15:-1], 16))  # 16 Stands for the base


# webbrowser.open_new_tab("https://www.apple.com")
###################################################################################################################################################
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """
        # Calculate total seconds to represent
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600  # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):  # A way to print a class
        timeString = ""
        if self.hours < 10:
            timeString += "0"
        timeString += str(self.hours) + ":"
        if self.minutes < 10:
            timeString += "0"
        timeString += str(self.minutes) + ":"
        if self.seconds < 10:
            timeString += "0"
        timeString += str(self.seconds)
        return timeString

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):  # Operator overloading
        secs = self.to_seconds() + other.to_seconds()
        return MyTime(0, 0, secs)


currentTime = MyTime(6, 32, 40)
breadTime = MyTime(3, 35, 50)
doneTime = currentTime + breadTime
print(doneTime)
