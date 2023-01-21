from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from base.screenshot import Screenshot
from pages.refund_page import RefundPage


class LaunchPage(Screenshot):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    #locators

    DEPART_FROM = 'flight_origin'
    GOING_TO = "flight_destination"
    GOING_TO_RESULT_FIELD = "//div[@class='viewport']/div/div/li"
    SELECT_DATE_FIELD = "//*[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    REFUND_BUTTON = "//input[@value='Check Your Refund']"

    def getdepartfromfeild(self):
        return self.driver.find_element(By.NAME, self.DEPART_FROM)

    def getgoingtofeild(self):
        return self.driver.find_element(By.NAME, self.GOING_TO)

    def getgoingtoresults(self):
        return self.driver.find_elements(By.XPATH, self.GOING_TO_RESULT_FIELD)

    def getdatefield(self):
        return self.driver.find_element(By.XPATH, self.SELECT_DATE_FIELD)

    def getalldates(self):
        return self.driver.find_elements(By.XPATH, self.ALL_DATES)

    def getrefundbutton(self):
        return self.driver.find_element(By.XPATH, self.REFUND_BUTTON)

    def enterfromdepartlocation(self, departlocation):
        self.getdepartfromfeild().click()
        time.sleep(2)
        self.getdepartfromfeild().send_keys(departlocation)
        time.sleep(10)
        self.getdepartfromfeild().send_keys(Keys.ENTER)
        time.sleep(5)

    # def depart_from(self, departlocation):
    # depart_from = self.driver.find_element(By.NAME, "flight_origin")
    # depart_from.click()
    # time.sleep(2)
    # depart_from.send_keys(departlocation)  # "New"
    # time.sleep(2)
    # depart_from.send_keys(Keys.ENTER)
    # time.sleep(10)

    def entergoingtolocation(self, goinglocation):
        self.getgoingtofeild().send_keys(goinglocation)
        time.sleep(10)
        suggestions = self.getgoingtoresults()
        print(len(suggestions))
        for i in suggestions:
            print(i.text)
            if "New York (JFK)" in i.text:
            #if i.text == selectlocation:
                i.click()
                break
                time.sleep(5)
                # break

    # def going_to(self, goinglocation):
    # going_to = self.driver.find_element(By.NAME, "flight_destination")
    # going_to.send_keys(goinglocation)  # "New"
    # time.sleep(3)
    # suggestions = self.driver.find_elements(By.XPATH, "//div[@class='viewport']/div/div/li")
    # print(len(suggestions))
    # for i in suggestions:
    # print(i.text)
    # if "New York (JFK)" in i.text:
    # i.click()
    # time.sleep(3)
    # break
    def enter_select_date(self, depaturedate):
        self.getdatefield().click()
        time.sleep(5)
        all_dates = self.getalldates()
        for dates in all_dates:
            if dates.get_attribute("data-date") == depaturedate:
                dates.click()
                time.sleep(5)
                break

    # def select_date(self):
    # self.driver.find_element(By.XPATH, "//*[@id='BE_flight_origin_date']").click()
    # time.sleep(5)
    # all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

    # for dates in all_dates:
    # if "24/02/2023" in dates.get_attribute("data-date"):
    # dates.click()
    # time.sleep(5)
    # break

    def enter_check_refund(self):
        # self.driver.find_element(By.XPATH, "//input[@value='Check Your Refund']").click()
        self.getrefundbutton().click()
        time.sleep(5)

    def searchflights(self,departlocation,goingtolocation,depaturedate):
        self.enterfromdepartlocation(departlocation)
        self.entergoingtolocation(goingtolocation)
        self.enter_select_date(depaturedate)
        self.enter_check_refund()
        refund_page_result = RefundPage(self.driver, self.wait)
        return refund_page_result
    def load_again(self):
        self.driver.get("https://www.yatra.com")
