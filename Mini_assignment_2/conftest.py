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


input1 = ("2023-06-06", "12:00", "2023-06-07", "12:00")
input2 = ("2023-06-14", "09:00", "2023-06-14", "11:00")


@pytest.fixture(params=[input1, input2])
def test_data(request):
    return request.param
