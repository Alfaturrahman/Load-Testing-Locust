import csv
import random

valid_users = [
    {"email": "user@example.com", "password": "Password123"}
]

invalid_users = [
    {"email": "user@example.com", "password": "WrongPassword"},
    {"email": "invalid@example.com", "password": "Password123"},
    {"email": "", "password": "Password123"},
    {"email": "user@example.com", "password": ""},
    {"email": "", "password": ""},
    {"email": "notanemail.com", "password": "abc123"}
]

# Tambahkan user random invalid
for i in range(10):
    invalid_users.append({
        "email": f"invalid{i}@example.com",
        "password": random.choice(["", "wrongpass", "123456"])
    })

# Simpan valid user
with open("users_valid.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["email", "password"])
    writer.writeheader()
    writer.writerows(valid_users)

# Simpan invalid user
with open("users_invalid.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["email", "password"])
    writer.writeheader()
    writer.writerows(invalid_users)

print("✅ users_valid.csv & users_invalid.csv berhasil dibuat!")
