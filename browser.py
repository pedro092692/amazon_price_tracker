import requests


class Browser:

    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
            "Accept-Encoding": 'gzip, deflate, br',
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cookie": "PHPSESSID=80a404e056194953445c09a9e4f9c228; _ga=GA1.2.504228614.1701722106; _gid=GA1.2.1057656055.1701722106; _ga_VL41109FEB=GS1.2.1701722106.1.1.1701722933.0.0.0"

        }

    def get_webpage(self):
        try:
            response = requests.get(self.url, params={"User-Agent": "Defined"})
            response.raise_for_status()
            result = response.text
        except requests.exceptions.HTTPError:
            print("Sorry there was a problem with the connection.")
        else:
            return result

