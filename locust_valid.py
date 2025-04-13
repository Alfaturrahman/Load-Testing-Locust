from locust import HttpUser, task, between
import csv
import random

class ValidLoginTest(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.users = []
        with open("users_valid.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.users.append(row)

    @task
    def login_test(self):
        user = random.choice(self.users)
        response = self.client.post("/login", json={
            "email": user["email"],
            "password": user["password"]
        })
        print(f"[VALID] {response.status_code} → {user['email']}")
