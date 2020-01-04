import time
from random import *

alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Bangalore', 'Hyderabad', 'Mumbai', 'Delhi', 'Pune']
designation = ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead', 'Program Manager']


# below code is for getting the fake name where name should range from 3 to 10 letters and first letter should be
# capital

def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2, 9)
    for i in range(n):
        name = name + choice(alphabets)
    return name


# below code is to get emp number which should start from "E-" EX- E-1234

def get_fake_eno():
    eno = 'E-'
    for i in range(4):
        eno = eno + choice(digits)
    return eno


# below code is to get salary which should range from 10000 to 50000 and should be float number

def get_fake_sal():
    sal = uniform(10000, 50000)
    return sal


# below code is to get city for the employee

def get_fake_city():
    city = choice(cities)
    return city


# Below code is to generate phone number for a employee where it should start from (6,7,8,9) and must be 10 digits only

def get_fake_mno():
    mno = choice('6789')
    for i in range(9):
        mno = mno + choice(digits)
    return mno


# Below code is to generate designation for the employee

def get_fake_designation():
    des = choice(designation)
    return des


# Below code is to generate the data of the employee

def get_fake_emp_data():
    print("Employee name: ", get_fake_name())
    print("Employee number: ", get_fake_eno())
    print("Employee salary: {:.2f} ".format(get_fake_sal()))
    print("Employee city: ", get_fake_city())
    print("Employee contact number: ", get_fake_mno())
    print("Employee designation: ", get_fake_designation())


for i in range(10):
    get_fake_emp_data()
    print()

time.sleep(10)