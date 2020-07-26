import os

user = os.environ.get('USER')
password = os.environ.get('PASS')


for el in os.environ.items():
    print(el)

print(user,password)
