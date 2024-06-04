# amazon price tracker project

from browser import Browser
from scraper import Scraper
from price_compare import Compare
from mail_sender import Email

# Please put your amazon product url and the top price
url_product = "https://www.amazon.com/Gigabyte-GeForce-WINDFORCE-Graphics-GV-N4070WF3OC-12GD/dp/B0BZDYZ4V5/ref=sr_1_2?crid=30GFOKPISLKKK&keywords=rtx%2B4070&qid=1701726171&sprefix=rtx%2B%2Caps%2C126&sr=8-2&th=1"
product_top_price = 840

browser = Browser(url_product)
# Get webpage of the product
product_page = browser.get_webpage()
email = Email()

if product_page:
    # Scraping price
    scraper = Scraper(product_page)
    product_info = scraper.get_data()
    # Comparing prices
    compare = Compare(product_info["product_price"], product_top_price)
    if compare.price_compare():
        # send email
        print("sending email")
        email.send_email(product_info)
