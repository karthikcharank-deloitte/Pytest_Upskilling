import inspect
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # service_obj = Service("C:\\Softwares\\Webdrivers\\chromedriver.exe")
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(service=service_obj, options=option)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    # driver.close()


def getLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler("../Mini_assignment_5/Reports/logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.handlers = []
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    return logger

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
