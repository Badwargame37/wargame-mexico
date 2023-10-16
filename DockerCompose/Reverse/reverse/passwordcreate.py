from werkzeug.security import generate_password_hash

passwords = ["Flag123", "internet", "500379d15e1f3c1ca605168b62f367cbdab8abde2b64f236972903f9ff3f63a5", "tequiero"]

hashed_passwords = [generate_password_hash(password) for password in passwords]

print("Hashed Passwords: ", hashed_passwords)
