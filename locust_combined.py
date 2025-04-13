from locust import HttpUser, task, between
import csv
import random

class CombinedLoginTest(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.users = []
        
        # Load valid users
        with open("users_valid.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["type"] = "VALID"
                self.users.append(row)
        
        # Load invalid users
        with open("users_invalid.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["type"] = "INVALID"
                self.users.append(row)

    @task
    def login_test(self):
        user = random.choice(self.users)
        response = self.client.post("/login", json={
            "email": user["email"],
            "password": user["password"]
        })

        print(f"[{user['type']}] {response.status_code} → {user['email']}")
