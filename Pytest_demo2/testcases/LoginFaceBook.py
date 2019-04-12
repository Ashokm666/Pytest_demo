import unittest

from selenium.webdriver import Chrome
import HtmlTestRunner
class LoginFaceBookpage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=Chrome(r"C:\Users\windows 8\PycharmProjects\Pytest_demo2\driver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_LoginHome(self):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element_by_id('email').send_keys("ashokm1712@yahoo.com")
        self.driver.find_element_by_id('pass').send_keys("asdjbns123")
        self.driver.find_element_by_css_selector('#u_0_2').click()


    def test_CreateAccount(self):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element_by_id('u_0_j').send_keys("heloooooooooo")
        self.driver.find_element_by_css_selector('#u_0_11').click()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("C:/na"))

        