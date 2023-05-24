import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = None
input1 = ("2023-06-06", "12:00", "2023-06-07", "12:00", "chrome")
input2 = ("2023-06-14", "09:00", "2023-06-14", "11:00", "firefox")


@pytest.fixture(scope="class")
def setup(request, test_data):
    global driver
    if test_data[4] == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif test_data[4] == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(params=[input1, input2], scope="module")
def test_data(request):
    return request.param
