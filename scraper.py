from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, web):
        self.web_page = web
        self.soup = BeautifulSoup(self.web_page, "html.parser")

    def get_data(self):
        data = self.soup
        product_price = data.find(name='span', class_='a-offscreen')
        product_name = data.find(name='span', id='productTitle')

        product_info = {
            "product_name": product_name.text,
            "product_price": float(product_price.text.replace("$", ""))
        }
        return product_info

