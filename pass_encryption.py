import hashlib
from password_generator.pass_gen import password
from password_generator.pass_gen import pass_file
hashed=hashlib.new('sha256')
hashed.update(f"{password}".encode())
print("your encrypted password is:",hashed.hexdigest())
pass_file(hashed.hexdigest())