from selenium.webdriver.common.by import By


class LoginPage:
    input_box_email_id = "Email"
    input_box_password_id = "Password"
    login_button_css_selector = "button[type='submit']"
    logout_button_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.input_box_email_id).clear()
        self.driver.find_element(By.ID, self.input_box_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.input_box_password_id).clear()
        self.driver.find_element(By.ID, self.input_box_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()


# if __name__ == '__main__':
#     url = "https://admin-demo.nopcommerce.com/"
#     driver_ = Firefox()
#     driver_.implicitly_wait(time_to_wait=10)
#     driver_.maximize_window()
#     driver_.get(url=url)
#
#     lp = LoginPage(driver=driver_)
#     lp.set_email(email="admin@yourstore.com")
#     lp.set_password(password="admin")
#     lp.login()
#     time.sleep(2)
#     lp.logout()
#     time.sleep(3)
#     driver_.quit()
