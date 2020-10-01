'''
Created on 28 Sep 2020

@author: 611104661
'''
#from selenium.webdriver.support.ui import Select
from Utilities.BaseClassA import BaseClassA
from PageObject.HomePage import HomePage
import pytest
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClassA):

    def test_formSubmission(self,getData):
        
        log=self.test_getLogger()
        homepage=HomePage(self.driver)
        log.info("Entering data for form submission")
        log.info("Name is"+getData["Firstname"])
        homepage.getname().send_keys(getData["Firstname"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys("123456")
        homepage.getCheckMe().click()
        
        self.selectOptionbyVisibleText(homepage.getGender(), getData["Gender"])
        #=======================================================================
        # mygender=Select(homepage.getGender())
        # mygender.select_by_visible_text("Female")
        #=======================================================================
        homepage.getStatus().click()
        homepage.getDateofBirth().send_keys("12/03/1991")
        homepage.getSubmit().click()
        message=homepage.getAlertMsg().text

        #for substring match
        assert "Success" in message 
        #assert "Success! The Form has been submitted successfully!." == message 
        self.driver.refresh()
        
    #Passing data by tuple & dictionary    
    #@pytest.fixture(params=[("Shivangi","Maurya@gmail.com","Female"),("Krishna","Kumar@gmail.com","Male")])
    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self,request):
        return request.param
