
class Makemytrip_Pageobject():

    def __init__(self,driver):
        self.driver=driver

        self.text_from_css="input[class='react-autosuggest__input react-autosuggest__input--open']"
        self.button_search_xpath="//a[text()='Search']"
        self.closeadv_css="i[class='wewidgeticon we_close']"

    def fromtext(self,fromto):
        self.driver.find_element_by_css_selector(self.text_from_css).send_keys(fromto)

    def clicksearch(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    def closeAdv(self):
        self.driver.find_element_by_css_selector(self.closeadv_css).click()

class Paytm_pageobject():

    def __init__(self,driver):
        self.driver=driver
        self.button_cableTv_xpath="//span[text()='CableTv']"
        self.text_opeartor_css="input[autocomplete='new-password']"

    def clickCableTv(self):
        self.driver.find_element_by_xpath(self.button_cableTv_xpath).click()

    def EnterOperatorText(self,opartor):
        self.driver.find_element_by_css_selector(self.text_opeartor_css).send_keys(opartor)