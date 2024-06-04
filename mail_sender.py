import smtplib
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

class Email:

    def __init__(self):
        self.server = os.environ.get('SERVER')
        self.user = os.environ.get('USER')
        self.password = os.environ.get('PASSWORD')
        self.port = 587

    def send_email(self, product_info):
        with smtplib.SMTP(self.server, self.port) as connection:
            connection.starttls()
            connection.login(self.user, self.password)
            connection.sendmail(from_addr=self.user, to_addrs=self.user, msg=f"Subject:Price Notification\n\n"
                                                                             f"Hurry up! Your product: \n"
                                                                             f"{product_info['product_name']} \n"
                                                                             f"now cost: "
                                                                             f"${product_info['product_price']}")

