import json
with open("text.json") as data_file: 
    data=json.loads(data_file)

user=data['users']

for user in data:
  counter=0
  print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
  while counter < len(user['details']):
      print ("users mobile number is " + user['details'][counter]['mobileNo'])
      print ("users age  is " + user['details'][counter]['age'])
      print ("users city is " + user['details'][counter]['city'])