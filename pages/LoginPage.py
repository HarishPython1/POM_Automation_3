from selenium import  webdriver
class Login:
    def __init__(self,driver):
        self.driver=driver
    def acti_login(self,un,pwd):
        # Login
        self.driver.find_element_by_id("username").send_keys(un)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_xpath("//*[text()='Login ']").click()