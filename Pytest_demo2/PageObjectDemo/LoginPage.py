
class LoginPages():



    def __init__(self,driver):
        self.driver=driver
        self.text_email_id = 'email'
        self.text_password_id = 'pass'
        self.button_login_css = '#u_0_2'

        self.text_firstname_id = 'u_0_j'
        self.button_signup_css = '#u_0_11'

    def email_textBox(self,email):
        self.driver.find_element_by_id(self.text_email_id).send_keys(email)

    def password_textbox(self,password):
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def Loginbutton(self):
        self.driver.find_element_by_css_selector(self.button_login_css).click()

    def firstName(self,firstname):
        self.driver.find_element_by_id(self.text_firstname_id).send_keys(firstname)

    def SignUpButton(self):
        self.driver.find_element_by_id(self.button_signup_css).click()