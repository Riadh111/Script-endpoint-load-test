from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def login(self):
            chatbot_response=self.client.post(
            url="https://empower-1for1.alwaysdata.net/chatbot/generate-response",
            headers={
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryuwwAZ3cBP81LNKc4',
                'cookie': 'PHPSESSID=9ccfbff673c7a0c81289d4f71835694b; typography=poppins; version=light; layout=vertical; headerBg=color_1; primary=color_1; navheaderBg=color_1; sidebarBg=color_1; sidebarStyle=full; sidebarPosition=fixed; headerPosition=fixed; containerLayout=full; navTextColor=; navigationBarImg=; direction=ltr; XSRF-TOKEN=eyJpdiI6IlhMdWFRTFRyTHN5WHVYb2RIelFpR1E9PSIsInZhbHVlIjoiU0RJMlVqK1Q1eDlRQXU3WEt1TDFOWXZqUXJ3MVJsTTR1cUpKSmlyMENMTWYwZWpuandsczMrMjhBc1JRZURiVHBNQk02QkVmS3FSaVgxS0pLQUlSVHY1RjRCZE1nQVppa1orZjBrNEhKNVhvUXJoU2tLUVVrWVhXcnF6MlR1ajAiLCJtYWMiOiJjODc0MjJiYjhmODA0YmM1MjZlNTU4ZjEyYjVlYzdmMTIwNzI4ZjJlYjgzNjk0NTRiZDJlYzlhYWE0YTMxYmFjIiwidGFnIjoiIn0%3D; empower_1for1_session=eyJpdiI6Im5TUWdZQVVFREZ6V01rZitmNCtNaUE9PSIsInZhbHVlIjoicEZ3NUlyejgzbUdFbnFydnpOTDRBS1oySUtiQTVVN1k3MDJoTGJ5cGdPckEzNXR1cEVFaFRkSms5V3Zmbm5tNnFxNEZxSkRHTmNBMVU4cTUrY1VWUUk0WHRKVG9OMnJ2cXNQYU9wc3MvaVBMNE9XZWRDK2JEZUtUbXJnb0ZhbWYiLCJtYWMiOiIxYThhMzNjOTBkNGNiODcyYzgxNzBhMjc3ZmE1ZGZkMWYxZWMxNzMyMWJlMzE3NDhmZTAwNzJhZWNkN2EwNGQ5IiwidGFnIjoiIn0%3D',
                'origin': 'https://empower-1for1.alwaysdata.net',
                'priority': 'u=1, i',
                'referer': 'https://empower-1for1.alwaysdata.net/mathematiques/theme/nombres-complexes-et-trigonom%C3%A9trie--math-/build-skills/course/1',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'emapty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'x-csrf-token': 'QJgsaF2xi8M6XnSAUnYhndZOTgh2xhOqy99Ddea0',
                'x-requested-with': 'XMLHttpRequest'
            },
            data={
                "chatbot_message": "d_o_n_n_e_r_e_x_a_m_p_l_e_d_e_n_o_m_b_r_e_c_o_m_p_l_e_x_e_s\\",  
                "chatbot_ordonner_stuck": "",  
                "chatbot_path_used_image": "",  
                "chatbot_etape_id": "",
                "chatbot_question_id": "undefined",
                "chatbot_prb_question_id": "",
                "chatbot_topic_id": "10",
                "mode_chatbot": "course"
            }
            )
            print("Chatbot response status code:", chatbot_response.status_code)
            print("Chatbot response content:", chatbot_response.text) 