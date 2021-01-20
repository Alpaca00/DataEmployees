import random
import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.itproger
collection = db.employees


lettersV = ['a', 'e', 'i', 'o', 'u']
lettersC = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
symbols = ['.','-', '_']
symbolAt = '@'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


count = 0

while count < 10000:
    nr_lettersName = random.randint(3, 4)
    nr_lettersSurname = random.randint(3, 4)
    nr_numbersPhone = random.randint(7, 11)
    nr_lettersAddress = random.randint(5, 11)
    name = ""
    for char in range(1, nr_lettersName + 1):
        rand_charC = random.choice(lettersC)
        rand_charV = random.choice(lettersV)
        name += rand_charV + rand_charC
    surname = ""
    for char in range(1, nr_lettersSurname + 1):
        rand_charC = random.choice(lettersC)
        rand_charV = random.choice(lettersV)
        surname += rand_charC + rand_charV
    phone = ""
    for char in range(1, nr_numbersPhone + 1):
        rand_char = random.choice(numbers)
        phone += rand_char
    before = ""
    after = ""
    for char in range(1, 4):
        first = random.choice(lettersC)
        second = random.choice(lettersV)
        before += first
        after += second

    randomSymbol = random.choice(symbols)
    email = f"{name}{randomSymbol}{surname}{symbolAt}{before}.{after}"
    address = ""
    for char in range(1, nr_lettersAddress + 1):
        rand_charV = random.choice(lettersV)
        rand_charC = random.choice(lettersC)
        address += rand_charC + rand_charV
    count += 1
    post2 = collection.insert_one({'name': name.title(), 'surname': surname.title(), 'phone': phone, 'email': email, 'address': address.title()})
