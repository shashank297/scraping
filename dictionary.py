import requests
import json
import os
from datetime import datetime

class DreamDictionaryScraper:
    def __init__(self):
        self.base_url = "https://dream-interpreter-ai-python.onrender.com/dictionary/initial/"
        self.request_header = {
            "authority": "dream-interpreter-ai-python.onrender.com",
            "method": "GET",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://dreaminterpreter.ai",
            "pragma": "no-cache",
            "referer": "https://dreaminterpreter.ai/",
            "sec-ch-ua": '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

    def fetch_data(self, letter):
        with requests.Session() as session:
            url = f"{self.base_url}{letter}"
            response = session.get(url, headers=self.request_header)

        if response.status_code == 200:
            json_data = json.loads(response.content.decode("utf-8"))
            return json_data
        else:
            print(f"Error fetching data for letter {letter}: {response.status_code}")
            return None

    def save_response_to_file(self, letter, data):
        current_date = datetime.now().strftime("%Y-%m-%d")
        output_folder = "output"
        dictionary_folder = os.path.join(output_folder, "dictionary")
        os.makedirs(dictionary_folder, exist_ok=True)
        filename = os.path.join(dictionary_folder, f"dictionary_{letter}_{current_date}.json")

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")

# Create an instance of DreamDictionaryScraper
dictionary_scraper = DreamDictionaryScraper()

# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Fetch data for each letter
for letter in alphabet:
    data = dictionary_scraper.fetch_data(letter)
    if data:
        dictionary_scraper.save_response_to_file(letter, data)
