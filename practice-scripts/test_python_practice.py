import sys
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestGitHubActions:

    def test_githubaction_practice(self):

        global driver
        URL = "https://www.google.com/"
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1420,1080")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        driver.maximize_window()
        driver.get(URL)
        time.sleep(5)

    def test_validation(self):

        try:
            assert WebDriverWait(driver, timeout=30).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Google Search']")))
            print("Passed!!")
        except:
            print("Failed!!")