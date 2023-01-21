from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


class Screenshot:
    def __init__(self, driver):
        self.driver = driver


    def screen_shot(self):
        self.driver.get_screenshot_as_file("C:\\Users\\uif48567\\PycharmProjects\\PythonFramework\\screenshots\\image.png")



