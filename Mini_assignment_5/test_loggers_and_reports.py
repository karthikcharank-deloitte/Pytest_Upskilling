import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from conftest import getLogger


@pytest.mark.usefixtures("setup")
class Test:

    def test_calculate_cost(self):
        log = getLogger()
        # Launch URL
        self.driver.get("https://practice.expandtesting.com/webpark")
        log.info("URL launched successfully..!!")
        # Set Short-Term Parking
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='parkingLot']"))
        select.select_by_value("ShortTerm")
        log.info("Parking type selected as: Short-Term parking")
        # Set Entry Date
        self.driver.find_element(By.XPATH, "//input[@id='entryDate']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='entryDate']").send_keys("2023-06-06")
        log.info("Entry date is set to: 2023-06-06")
        # Set Entry Time
        self.driver.find_element(By.XPATH, "//input[@id='entryTime']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='entryTime']").send_keys("09:00")
        log.info("Entry time is set to: 09:00")
        # Set Exit Date
        self.driver.find_element(By.XPATH, "//input[@id='exitDate']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='exitDate']").send_keys("2023-06-06")
        log.info("Exit date is set to: 2023-06-06")
        # Set Exit Time
        self.driver.find_element(By.XPATH, "//input[@id='exitTime']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='exitTime']").send_keys("11:00")
        log.info("Exit time is set to: 11:00")
        # Click Calculate Cost button
        self.driver.find_element(By.XPATH, "//button[@id='calculateCost']").click()
        log.info("Clicked on Calculate cost button")

    def test_verify_cost_and_time(self):
        log = getLogger()
        # Get Cost and Time
        expected_cost = "4.00€"
        expected_time = "0 Day(s), 2 Hour(s), 0 Minute(s)"
        actual_cost = self.driver.find_element(By.XPATH, "//b[@id='resultValue']").text
        log.info("The actual cost for parking: " + actual_cost)
        actual_time = self.driver.find_element(By.XPATH, "//b[@id='resultMessage']").text
        log.info("The actual time for parking: " + actual_time)
        # Assert Cost and Time
        assert actual_cost == expected_cost
        assert actual_time == expected_time
        log.info("The cost and time for the parking is verified successfully..!!")

    def test_booking_details(self):
        log = getLogger()
        # Clicking Reserve Online button
        self.driver.find_element(By.XPATH, "//a[@id='reserveOnline']").click()
        log.info("Clicked on Reserve Online")
        # Adding Personal Details
        self.driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("ABC")
        log.info("First name entered is: ABC")
        self.driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("XYZ")
        log.info("Last name entered is: XYZ")
        # Adding Contact Details
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("abc@gmail.com")
        log.info("E-mail entered is: abc@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9876543210")
        log.info("Mobile number entered is: 9876543210")
        # Adding Vehicle Information
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='vehicleSize']"))
        select.select_by_visible_text("Medium car")
        log.info("Vehicle size entered as: Medium Car")
        self.driver.find_element(By.XPATH, "//input[@id='lpNumber']").send_keys("AB1234")
        log.info("Vehicle number entered as: AB1234")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log.info("Scrolled down to the bottom of the webpage")
        # Click Book now
        submit_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_btn)
        log.info("Clicked on submit button")

    def test_verify_reservation(self):
        log = getLogger()
        # Assert title of the webpage
        title = self.driver.title
        log.info("The title of the webpage is: " + title)
        assert title == "Web Parking Payment"
        log.info("The title of the webpage is verified successfully..!!: ")
