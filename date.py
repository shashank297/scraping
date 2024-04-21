import requests
import datetime
import json
import os

class DreamScraper:
    def __init__(self):
        self.request_header = {
            "Authority": "dream-interpreter-ai-python.onrender.com",
            "Method": "GET",
            "Path": "/art",
            "Scheme": "https",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.6",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "Language": "en",
            "Origin": "https://dreaminterpreter.ai",
            "Pragma": "no-cache",
            "Referer": "https://dreaminterpreter.ai/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Gpc": "1",
            "Timezone": "Asia/Calcutta",
            "Uid": "a02ee7a8-e3b8-43a4-a614-32bceac3ee4b",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

    def date_to_milliseconds(self, date_string):
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        milliseconds = int(date.timestamp() * 1000)
        return milliseconds

    def make_request_with_date(self, date_string):
        date = self.date_to_milliseconds(date_string)
        with requests.Session() as session:
            url = "https://dream-interpreter-ai-python.onrender.com/art"
            params = {"date": date}
            response = session.get(url, params=params, headers=self.request_header)

        if response.status_code == 200:
            json_data = json.loads(response.content.decode("utf-8"))
            return json_data
        else:
            print("Error:", response.status_code)
            return None

    def create_folder_if_not_exists(self, folder_path):
        if not os.path.exists(os.path.join(folder_path,"Date")):
            os.makedirs(os.path.join(folder_path,"Date"))

    def scrape_data_from_date_range(self, start_date_string, end_date_string, output_folder):
        self.create_folder_if_not_exists(output_folder)

        start_date = datetime.datetime.strptime(start_date_string, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_string, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            date_string = start_date.strftime("%Y-%m-%d")
            json_output = self.make_request_with_date(date_string)

            if json_output:
                output_file = os.path.join(output_folder,"Date", f"output_{date_string}.jsonl")
                with open(output_file, 'a') as f:
                    f.write(json.dumps(json_output['dreams']) + '\n')

            start_date += delta

# Test the DreamScraper class
scraper = DreamScraper()
start_date = "2024-01-01"
end_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Current date
output_folder = f"output"
scraper.scrape_data_from_date_range(start_date, end_date, output_folder)
