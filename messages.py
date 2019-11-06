import requests
from Crypto.PublicKey import RSA 

key_response = None
with open('key.rsa') as file:
    key_response = file.read().encode()

# user = 'malinok3'
# base_url = 'http://10.11.14.210/message'
# 'http://10.11.14.210/key/nowyNick'
# url = f'{base_url}/{user}'

# mes = {'message': 'LAST CHRISTMAS'}

# r = requests.get('http://google.com')
# r = requests.post(url, json=mes)


# # Tworzenie kluczy RSA 
# rsa_keys = RSA.generate(1024) 
# # Wydzielenie klucza publicznego 
# pub_key = rsa_keys.publickey() 
# # Zaszyfrowanie przy pomocy klucza publicznego 
# encrypted = pub_key.encrypt(r.text, "hello") 
# # Odszyfrowanie kluczem prywatnym 
# # print(rsa_keys.decrypt(encrypted))
# r = requests.post(url)

user = 'deadbeef'
base_url = 'http://10.11.14.210'
url = f'{base_url}/keys/{user}'
print(url)
# r = requests.get(url)
# public_key = r.text
public_key = key_response

public_key = RSA.importKey(public_key.decode())
print(public_key)
message = 'hello'
encrypted_message = public_key.encrypt(message.encode(), 'smiecia')


d = {'message' : encrypted_message}
print(d)
# r = requests.post(url, json=d)

key = None
with open('key_priv.rsa') as file:
    key = RSA.importKey(file.read())

print('Decrypted')
print(key.decrypt(encrypted_message).decode())


# print(r.status_code)
# print(r.text)

