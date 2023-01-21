from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from base.screenshot import Screenshot


class RefundPage(Screenshot):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    #locators
    LOGIN = "email-mobile-input"
    LOGIN_ID = "mb-brn"
    SUBMIT= "mb-continue-btn"

    def getenterphonenumber(self):
        return self.driver.find_element(By.NAME,self.LOGIN)
    def getenterticketid(self):
        return self.driver.find_element(By.ID,self.LOGIN_ID)
    def getsubmit(self):
        return self.driver.find_element(By.ID,self.SUBMIT)


    def login_details(self):
        self.getenterphonenumber().send_keys("6302414526")
        time.sleep(5)
        self.getenterticketid().send_keys("ASHGGHFGFJFGFHG")
        time.sleep(2)
        self.getsubmit().click()
        time.sleep(5)
        #self.driver.find_element(By.NAME, "email-mobile-input").send_keys("6302414526")
        #time.sleep(2)
        #self.driver.find_element(By.ID, "mb-brn").send_keys("AGJKFGVBJNJJH")
        #self.driver.find_element(By.ID, "mb-continue-btn").click()
        #time.sleep(5)


