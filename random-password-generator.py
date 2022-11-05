import random
import string

password_length = int(input('\nLength of the password: '))

punctuations = string.punctuation
digits = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

combination = punctuations + digits + lowercase + uppercase

password = "".join(random.choices(combination,k=password_length))

print(password)