import time
import pytest
import unittest
from pages.yatra_launch_page import LaunchPage
from ddt import ddt, data, unpack,file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        # separating objects from main code
        self.lp = LaunchPage(self.driver, self.wait)

    # data driven testing
    #@data(("New", "New", "24/02/2023"),("Mumbai","New","31/01/2023"))
    #@unpack
    #@file_data("C:\\Users\\uif48567\\PycharmProjects\\PythonFramework\\testdata\\testdata.json") #for json
    @file_data("C:\\Users\\uif48567\\PycharmProjects\\PythonFramework\\testdata\\test.yaml") #for yaml
    def test_search_flights(self, departlocation,goingtolocation,depaturedate):
        """launch the browser
        #providing going from location"""
        refund_page_result = self.lp.searchflights(departlocation,goingtolocation,depaturedate)

        '''enter login details'''
        refund_page_result.login_details()
        time.sleep(10)

        '''screenshot'''
        self.lp.screen_shot()
        time.sleep(5)
        self.lp.load_again()
        time.sleep(5)
