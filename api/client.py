import requests
import random

link = 'http://127.0.0.1:5000/classification/'
link1 = 'http://127.0.0.1:5000/authenticatation/'
link2 = 'http://127.0.0.1:5000/analytics/'

api_key = 'b17ea0c58973657a4928af9cf4eaf0f378e7ebf1441b95b86253829d152e39085e8211d3e3ad7afdb62e6c4ad208da7a'
w_api_key = 'd7311caga7e3c8e6db309d9fe617fff192bddc5bd8877686d2cbdbeaf05d77aa6766d84a2716f8dc3427e91c34a6e24cc'
seed1 = random.choice(['male', 'female'])
data1 = {
    'api_key':api_key,
    'account_age':45,
    'avs':9425,
    'amount':60,
    'card_number':8771,
    'location':'Harare',
    'account_type':'Credit',
    'bank':'FBC Bank',
    'connection_type':'http',
    'cvv':'n',
    'broswer':'Mozilla/5.0 ',
    'gender':'female',
    'entry_type':'chip',
    'transaction_time':124,
    'account_balance':94,
    'holder_age':32
}

data3 = {
    'api_key': w_api_key,
    'account_age':305,
    'avs':475,
    'amount':15000,
    'card_number':8472,
    'location':'Harare',
    'account_type':'Credit',
    'bank':'FBC Bank',
    'connection_type':'https',
    'cvv':'n',
    'broswer':'Mozilla/5.0 ',
    'gender':'male',
    'entry_type':'chip',
    'transaction_time':54,
    'account_balance':2365,
    'holder_age':32
}
data2 = {
    'api_key': api_key,
    'account_age':305,
    'avs':475,
    'amount':15000,
    'card_number':8472,
    'location':'Harare',
    'account_type':'Credit',
    'bank':'FBC Bank',
    'connection_type':'https',
    'cvv':'n',
    'broswer':'Mozilla/5.0 ',
    'gender':'male',
    'entry_type':'chip',
    'transaction_time':54,
    'account_balance':2365,
    'holder_age':32
}
auth = {
   'client_id': 'd2fa7394034b409e97d936dfb3728422',
    'client_token': '9d261fe86923768a9c9f937a2bc93aff'
}

#obtaining API KEY
#resp = requests.get(link1, auth)
#print(resp.json())

#testing classification with wrong key
#resp = requests.get(link, data3)
#print(resp.json())

#classifying transaction 1
resp = requests.get(link, data3)
print(resp.json())

#classifying transaction 2
#resp = requests.get(link, data2)
#print(resp.json())
