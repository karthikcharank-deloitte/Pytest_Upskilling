import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
