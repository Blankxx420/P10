
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from djangoProject.settings import BASE_DIR
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class SeleniumRegisterTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(
            executable_path=str(BASE_DIR / 'webdrivers' / 'chromedriver'),
            options=chrome_options,)
        cls.selenium.implicitly_wait(10)
        cls.selenium.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_register(self):
        """Launches the functional_tests for the registration and automatical loggin feature"""
        # Access register page and fill fields
        self.selenium.get("%s%s" % (self.live_server_url, "/register/"))
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys("usertest1@email.com")
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys("usertest1")
        password_input = self.selenium.find_element(By.NAME,"password1")
        password_input.send_keys("Password+1234")
        confirm_password_input = self.selenium.find_element(By.NAME, "password2")
        confirm_password_input.send_keys("Password+1234")
        # Click on button which registers + login automatically
        self.selenium.find_element(By.XPATH, "//*[@id='register']/div/form/button").click()
        # Checks if icon "mon_compte" in DOM, means logged in
        self.selenium.find_element(By.ID, "mon_compte")