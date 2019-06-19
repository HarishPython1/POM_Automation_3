import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/BTM-Faculty/Downloads/chromedriver.exe")
    driver.get("http://localhost/login.do")
    driver.implicitly_wait(30)
    request.cls.driver = driver
    # yield
    # driver.quit()