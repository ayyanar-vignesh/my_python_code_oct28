url="https://rrgister_form"



#json->javascript object notation

# what is json?
# #json->javascript object notation
# it is used to storing and exchanging the datas

import json


actutal_data='{"firstname":"arun","lastname":"kumar","password":"1234"}'

data=json.loads(actutal_data)
print(data)


firstname=data['firstname']
lastname=data['lastname']
password=data['password']

print(f"my firstnamew is {firstname} ")
print(f"my lastname is {lastname}")
print(f"my password is {password}")
