from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def login(self):
        # Etape 1 : Ouvrir page Login et extraction du token
        response = self.client.get("https://empower-1for1.alwaysdata.net/login")  
        soup = BeautifulSoup(response.text, 'html.parser')
        token_input = soup.find("input", {"name": "_token"})
        # Etape 2 : Login avec token 
        if token_input and token_input.has_attr('value'):
            token = token_input['value']
            self.client.post("https://empower-1for1.alwaysdata.net/login", data={
                "username": "candidat2@gmail.com",  
                "password": "123456789",  
                "_token": token
            })
        # Etape 3 : Choisir "matiere" "mathematique"
            self.client.get("https://empower-1for1.alwaysdata.net/mathematiques/axis/build_skills_qcm/select-theme")

        # Etape 4 : Accéeder à "Je révise"
            self.client.get("https://empower-1for1.alwaysdata.net/mathematiques/revise/select-exam")

        # Etape 5 : Choisir un exercice 
            self.client.get("https://empower-1for1.alwaysdata.net/mathematiques/revise/exam/2/select-problem") 
            print(f"The token is: {token}")
        else:
            print("Token input element found, but no 'value' attribute.")
