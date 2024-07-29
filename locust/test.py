from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        # Perform the POST request to get the token
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/api/login", json={"email": "ake@gmail.com", "password": "123456"}, headers=headers)
        if response.status_code == 200:
            self.token = response.json().get("access_token")
            print(self.token )
        else:
            self.token = None

    @task
    def get_resource(self):
        if self.token:
            #headers = {"Authorization": f"Bearer {self.token}"}
            self.client.get("/api/category")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Simulate user wait time between requests
