import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class UnitTest(unittest.TestCase):
    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"
    WRONG_USER = "marco"
    WRONG_PASS = "123"

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.quit()

    #definim o functie care sa testeze o parola invalida
    def test_invalid_password(self):
        self.driver.find_element(By.ID, "username").send_keys(self.USERNAME)
        self.driver.find_element(By.ID, "password").send_keys(self.WRONG_PASS)
        self.driver.find_element(By.CLASS_NAME, "fa").click()
        print(self.driver.find_element(By.ID, "flash").text)
        assert self.driver.find_element(By.ID, "flash").text == "Your password is invalid!\n×"

    #definim o functie care sa testeze invalid user
    def test_invalid_user(self):
        self.driver.find_element(By.ID, "username").send_keys(self.WRONG_USER)
        self.driver.find_element(By.ID, "password").send_keys(self.PASSWORD)
        self.driver.find_element(By.CLASS_NAME, "fa").click()
        print(self.driver.find_element(By.ID, "flash").text)
        assert self.driver.find_element(By.ID, "flash").text == "Your username is invalid!\n×"

