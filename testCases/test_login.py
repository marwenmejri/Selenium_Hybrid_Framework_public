import time
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger1


class Test001Login:
    base_url = ReadConfig.get_app_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    logger = Logger1.sample_logger()

    @pytest.mark.run
    def test_login_page_title(self, setup):
        self.logger.info("***************** Test001Login ****************")
        self.logger.info("***************** Test Login Page Title ****************")
        self.driver = setup
        self.driver.get(url=self.base_url)
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            self.logger.info("***************** test_login_page_title IS PASSED ****************")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_login_page_title.png")
            self.logger.error("***************** test_login_page_title IS FAILED ****************")
            self.driver.quit()
            assert False

    @pytest.mark.run
    def test_login(self, setup):
        self.logger.info("***************** Test Login ****************")
        self.driver = setup
        self.driver.get(url=self.base_url)
        self.lp = LoginPage(driver=self.driver)
        self.lp.set_email(email=self.email)
        self.lp.set_password(password=self.password)
        self.lp.login()
        time.sleep(2)
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            self.logger.info("***************** test_login IS PASSED ****************")
            self.lp.logout()
            self.driver.quit()
            assert True
        else:
            self.logger.info("***************** test_login HAS FAILED ****************")
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.driver.quit()
            assert False

    def test_login_page_title1(self, setup):
        self.logger.info("***************** Test Login Page Title1 ****************")
        self.driver = setup
        self.driver.get(url=self.base_url)
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            self.logger.info("***************** test_login_page_title1 IS PASSED ****************")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_login_page_title1.png")
            self.logger.error("***************** test_login_page_title1 IS FAILED ****************")
            self.driver.quit()
            assert False

    def test_login1(self, setup):
        self.logger.info("***************** Test Login1 ****************")
        self.driver = setup
        self.driver.get(url=self.base_url)
        self.lp = LoginPage(driver=self.driver)
        self.lp.set_email(email=self.email)
        self.lp.set_password(password=self.password)
        self.lp.login()
        time.sleep(2)
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            self.logger.info("***************** test_login1 IS PASSED ****************")
            self.lp.logout()
            self.driver.quit()
            assert True
        else:
            self.logger.info("***************** test_login1 HAS FAILED ****************")
            self.driver.save_screenshot("Screenshots/test_login1.png")
            self.driver.quit()
            assert False
