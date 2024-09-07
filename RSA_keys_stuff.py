from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
import os
pathway = (os.path.dirname(__file__))

# Generating key pair
new_key = RSA.generate(2048)
private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

# Storing and encrypting private key in file
private_key_password = b'pm\x98H\x0c\x11\xfe\x80\xa6@\x9a\x98\xe3\xfe]\xe3'
cipher = AES.new(private_key_password, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(private_key)
file_out = open(f"{pathway}/server/private_key.pem", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

# PRINT FOR PROOF
# print('file_out: ')
# print(file_out)
file_out.close()

# Storing public key in file
fd = open(f"{pathway}/server/public_key.pem", "wb")
fd.write(public_key)
fd.close()

message = b'CODE EVERYDAY TO GET BETTER'

# Encrypt using key pair
key = RSA.import_key(open(f'{pathway}/server/public_key.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)

# PRINT FOR PROOF
# print('ciphertext: ')
# print(ciphertext)
# print('\n')

# Decrypt using key pair
file_in = open(f'{pathway}/server/private_key.pem', "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
file_in.close()
cipher = AES.new(private_key_password, AES.MODE_EAX, nonce)
private_key = cipher.decrypt_and_verify(ciphertext, tag)

# PRINT FOR PROOF
# print('private key: ')
# print(private_key)