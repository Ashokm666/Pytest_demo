import unittest
import pytest
import pytest_html
import time
from selenium.webdriver import Chrome
from page2.loginpage2 import Makemytrip_Pageobject
from page2.loginpage2 import Paytm_pageobject

class PaytmandMakeMytrip(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=Chrome(r"C:\\Users\\windows 8\\PycharmProjects\\Pytest_demo2\\driver\\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_TC1_makemytrip(self):
        driver=self.driver
        driver.get("https://www.makemytrip.com/")
        make_ref=Makemytrip_Pageobject(driver)
        time.sleep(10)
        make_ref.closeAdv()
        make_ref.fromtext("Banglore")
        make_ref.clicksearch()
        title=driver.title
        self.assertEqual(title,"Makemytrip","not matching the both")

    def test_TC2_paytm(self):
        driver=self.driver
        driver.get("https://paytm.com/")
        paytm_ref=Paytm_pageobject(driver)
        paytm_ref.clickCableTv()
        paytm_ref.EnterOperatorText("airtel")
        title=driver.title
        self.assertEqual(title,"Cable TV Recharge Online- Cable TV Recharge Offers and Bill Payment @ Paytm.com","not matching both")


if __name__ == "__main__":
    unittest.main()