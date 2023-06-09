import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test:

    def test_cost_and_time(self):
        # Launch URL
        self.driver.get("https://practice.expandtesting.com/webpark")
        # Set Entry Time
        self.driver.find_element(By.XPATH, "//input[@id='entryTime']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='entryTime']").send_keys("18:00")
        # Set Exit Time
        self.driver.find_element(By.XPATH, "//input[@id='exitTime']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='exitTime']").send_keys("18:00")
        # Click Calculate Cost button
        self.driver.find_element(By.XPATH, "//button[@id='calculateCost']").click()
        # Get Cost and Time
        expected_cost = "18.00€"
        expected_time = "1 Day(s), 0 Hour(s), 0 Minute(s)"
        actual_cost = self.driver.find_element(By.XPATH, "//b[@id='resultValue']").text
        actual_time = self.driver.find_element(By.XPATH, "//b[@id='resultMessage']").text
        # Assert Cost and Time
        assert actual_cost == expected_cost
        assert actual_time == expected_time
