import requests
import json
import os
from datetime import datetime

class DreamScraper:
    def __init__(self):
        self.request_header = {
            "authority":"dream-interpreter-ai-python.onrender.com",
            "method": "GET",
            "path": "/map/BR",
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

    def make_request_with_country(self, country_code):
        with requests.Session() as session:
            url = f"https://dream-interpreter-ai-python.onrender.com/map/{country_code}"
            response = session.get(url, headers=self.request_header)

        if response.status_code == 200:
            json_data = json.loads(response.content.decode("utf-8"))
            return json_data
        else:
            print("Error:", response.status_code)
            return None

    def save_response_to_file(self, country_code, data):
        current_date = datetime.now().strftime("%Y-%m-%d")
        output_folder = "output"
        country_folder = os.path.join(output_folder, "country", country_code)
        os.makedirs(country_folder, exist_ok=True)
        filename = os.path.join(country_folder, f"{country_code}_{current_date}.json")

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")


# Define the country codes dictionary
country_codes = {
    "United States": "US",
    "Brazil": "BR",
    "Russia": "RU",
    "Great Britain": "GB",
    "China": "CN",
    "Spain": "ES",
    "Canada": "CA",
    "Germany": "DE",
    "Mexico": "MX",
    "Colombia": "CO",
    "Pakistan": "PK",
    "Malaysia": "MY",
    "Italy": "IT",
    "Australia": "AU",
    "Romania": "RO",
    "South Africa": "ZA",
    "France": "FR",
    "Chile": "CL",
    "Taiwan": "TW",
    "Philippines": "PH",
    "Turkey": "TR",
    "Bangladesh": "BD",
    "Albania": "AL",
    "United Arab Emirates": "AE",
    "Venezuela": "VE",
    "Ukraine": "UA",
    "Nigeria": "NG",
    "Singapore": "SG",
    "Netherlands": "NL",
    "Thailand": "TH",
    "Kenya": "KE",
    "Indonesia": "ID",
    "Egypt": "EG",
    "Peru": "PE",
    "Poland": "PL",
    "Saudi Arabia": "SA",
    "Kazakhstan": "KZ",
    "Israel": "IL",
    "New Zealand": "NZ",
    "Ecuador": "EC",
    "Hong Kong": "HK",
    "Portugal": "PT",
    "Morocco": "MA",
    "South Korea": "KR",
    "Sri Lanka": "LK",
    "Belgium": "BE",
    "Sweden": "SE",
    "Greece": "GR",
    "Norway": "NO",
    "Ireland": "IE",
    "Belarus": "BY",
    "Oman": "OM",
    "Uzbekistan": "UZ",
    "India": "IN",
    "Bulgaria": "BG",
    "Uganda": "UG",
    "Japan": "JP",
    "Georgia": "GE",
    "El Salvador": "SV",
    "Austria": "AT",
    "Algeria": "DZ",
    "Switzerland": "CH",
    "Uruguay": "UY",
    "Bolivia": "BO",
    "Kuwait": "KW",
    "Qatar": "QA"
}

# Create an instance of DreamScraper
scraper = DreamScraper()

# Iterate over the country codes and fetch data
for country_name, country_code in country_codes.items():
    data = scraper.make_request_with_country(country_code)
    if data:
        scraper.save_response_to_file(country_code, data)
