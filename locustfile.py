from locust import HttpUser, task, between
import csv, random

class LoginUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.users = []
        with open("users.csv", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.users.append({
                    "email": row["email"],
                    "password": row["password"]
                })

    @task
    def login_test(self):
        user = random.choice(self.users)
        self.client.post("/login", json={
            "email": user["email"],
            "password": user["password"]
        })
