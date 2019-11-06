from Crypto.PublicKey import RSA

rsa_keys = RSA.generate(1024) 
# Wydzielenie klucza publicznego 

pub_key = rsa_keys.publickey()

with open('key.rsa', 'w') as file:
    file.write(pub_key.exportKey('PEM').decode())

with open('key_priv.rsa', 'w') as file:
    file.write(rsa_keys.exportKey('PEM').decode())

b'asdfa'