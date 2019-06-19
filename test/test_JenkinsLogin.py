from pages.LoginPage import Login
from data.testdata import *
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver=self.driver
        lp=Login(driver)
        lp.acti_login(USERNAME,PASSWORD)
# def test_logout():
#     #Logout
#     driver.find_element_by_id("logoutLink").click()


