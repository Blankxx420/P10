from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from chromedriver_binary import add_chromedriver_to_path


class SeleniumRegisterTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome("venv/lib/python3.9/site-packages/chromedriver_binary/chromedriver")
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_register(self):
        """Launches the functional_tests for the registration and automatical loggin feature"""
        # Access register page and fill fields
        self.selenium.get("%s%s" % (self.live_server_url, "/register/"))
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys("usertest1@email.com")
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("usertest1")
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys("Password+1234")
        confirm_password_input = self.selenium.find_element_by_name(
            "password2"
        )
        confirm_password_input.send_keys("Password+1234")
        # Click on button which registers + login automatically
        self.selenium.find_element_by_name("btn").click()
        # Checks if icon "mon_compte" in DOM, means logged in
        self.selenium.find_element_by_id("mon_compte")