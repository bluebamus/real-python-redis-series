from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):

    host = 'http://127.0.0.1:8000'
    wait_time = between(1, 2.5)

    @task
    def my_task(self):
        self.client.get("/cookbook/")