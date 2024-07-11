from locust import HttpUser, task, between
import re

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Time between task executions

    def on_start(self):
        self.xsrf_token = None
        self._token = None

    @task
    def save_request_qcm(self):
        # Step 1: Perform the GET request in Login to obtain tokens
        response = self.client.get("https://api-dev.empower-1for1.com/login")
        
        # Step 2: Extract XSRF-TOKEN from cookies
        self.xsrf_token = self.client.cookies.get('XSRF-TOKEN')
        print(f"self.xsrf_token : {self.xsrf_token}")    
        # Step 3: Extract _token from the response body
        match = re.search(r'name="_token" value="([^"]+)"', response.text)
        if match:
            self._token = match.group(1)
            print(f"_token : {self._token}")    
        if not self.xsrf_token or not self._token:
            print("Failed to retrieve tokens")
            return    
       

        data1 = {
            '_token': self._token,
            'email': 'candidat2@gmail.com',
            'password': '123456789'
        }
        # Perform a Post request to Login
        response2 = self.client.post("https://api-dev.empower-1for1.com/login", data=data1)
        # Perform Get to qcm 
        response3 = self.client.get("https://api-dev.empower-1for1.com/mathematiques/theme/limites-et-continuite-bac-math/build-skills/qcm")
       
        self.xsrf_token2 = self.client.cookies.get('XSRF-TOKEN')
        print(f"xsrf_token 2: '{self.xsrf_token2}'")    
        self.empower_1for1_session2 = self.client.cookies.get('empower_1for1_session')
        print(f"empower_1for1_session2 : '{self.empower_1for1_session2}'")   
        # Step 3: Extract _token from the response body
        match2 = re.search(r'name="_token" value="([^"]+)"', response3.text)

        self._token2 = match2.group(1)
        print(f"_token2 : '{self._token2}'")

        # Step 4: Perform the POST request to save qcm response using the extracted tokens
       

        data2 = {
            '_token': self._token2,
            'exercise_id': '21.056',
            'theme_id': '2',
            'duration': '00:10',
            'tentative': '',
            'propositons[]': '10051'
        }

        response4=self.client.post("https://api-dev.empower-1for1.com/save-request-qcm",data=data2)
        print(f"Response status code: {response4.status_code}")

