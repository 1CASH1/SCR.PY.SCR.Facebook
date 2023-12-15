from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from sleep_time import SleepTime


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.sleepTime = SleepTime()

    def login(self):
        sleep(self.sleepTime.generate_wait_time_random_m())
        self.driver.get("https://www.facebook.com")
        sleep(self.sleepTime.generate_wait_time("fast"))
        iptEmail = self.driver.find_element(
            By.ID, "email"
        )
        iptEmail.send_keys("cash.1dip1@hotmail.com")
        sleep(self.sleepTime.generate_wait_time("fast"))
        inptPass = self.driver.find_element(
            By.ID, "pass"
        )
        inptPass.send_keys("Fcada7131362##")
        sleep(self.sleepTime.generate_wait_time("fast"))
        btnLogin = self.driver.find_element("name", "login")
        btnLogin.click()
        sleep(self.sleepTime.generate_wait_time_random_m())
        btnPicture = self.driver.find_element(
            By.XPATH, '//*[@id="mount_0_0_jZ"]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div/svg/g/image')
        btnPicture.click()
        sleep(self.sleepTime.generate_wait_time("very_long"))
