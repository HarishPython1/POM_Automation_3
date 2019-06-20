from pages.WebGeneric import WebGeneric
class Login(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="username"
        self.pwd_name="pwd"
        self.login_btn_xpath="//*[text()='Login ']"
    def acti_login(self,un,pwd):
        # Login
        #wg=WebGeneric()
        #wg=WebGeneric(driver)

        # WebGeneric.enter(self.un_id,un)
        # WebGeneric.enter(self.pwd_name,pwd)
        # WebGeneric.submit(self.login_btn_xpath)
        wg=WebGeneric(self.driver)
        wg.enter(self.un_id,un)
        wg.enter(self.pwd_name,pwd)
        wg.submit(self.login_btn_xpath)

        #self.driver.find_element_by_id(self.un_id).send_keys(un)
        #self.driver.find_element_by_name(self.pwd_name).send_keys(pwd)
        #self.driver.find_element_by_xpath(self.login_btn_xpath).click()