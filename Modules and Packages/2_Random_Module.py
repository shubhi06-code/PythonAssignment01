import random
import string

otp = random.randint(100000, 999999)
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(12))
random_number = random.randint(1, 100)

print("OTP:", otp)
print("Random Password:", password)
print("Random List Number:", random_number)
