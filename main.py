import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "UserName"
PASSWORD = "PassWord"
NUM_OF_PAGES_TO_SCROLL_DOWN = 10

## chrome_driver_path
chrome_driver_path = "C:\Development\chromedriver"


class InstaFollower:

    def __init__(self, path):
        serv = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=serv)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.CSS_SELECTOR,
                                            "#loginForm > div > div:nth-child(1) > div > label > input")
        password = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > "
                                                             "label > input")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(4)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(5)

        modal = self.driver.find_element(By.CSS_SELECTOR, '._ab8w ._aano')
        print(modal)
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Chefsteps followers.
        people = self.driver.find_elements(By.CSS_SELECTOR,
                                           "._acap, a._acap, a._acap:visited")
        print(len(people))
        # To follow each follower in the pop-up.
        for persons in people:
            print(persons)
            try:
                persons.click()
            except ElementClickInterceptedException:
                try:
                    self.driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']").click()
                    continue
                except Exception:
                    print("Sorry, something went wrong")
                    pass
            time.sleep(2)


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
