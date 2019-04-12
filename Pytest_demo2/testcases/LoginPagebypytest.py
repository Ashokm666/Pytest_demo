import unittest
import pytest
from selenium.webdriver import Chrome

from PageObjectDemo.LoginPage import LoginPages


class LoginFaceBookpage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome(r"C:\Users\windows 8\PycharmProjects\Pytest_demo2\driver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_LoginHome(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        ref=LoginPages(driver)
        ref.email_textBox("ashokm1712@gmail.com")
        ref.password_textbox("ashok12245")
        ref.Loginbutton()

if __name__ == "__main__":
    unittest.main()
        #testRunner=HtmlTestRunner.HTMLTestRunner("C:/na"))

