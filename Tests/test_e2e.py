'''
Created on 25 Sep 2020

@author: 611104661
'''
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions
from PythonSelFramework.Utilities.BaseClassA import BaseClassA
from PageObject.HomePage import HomePage
#from PageObject.CheckoutPage import CheckoutPage
#from PageObject.ConfirmPage import ConfirmPage


class TestOne(BaseClassA):
    
    def test_e2e(self):
        
        log=self.test_getLogger()
        #Calling/defining Home Page constructor
        homepage=HomePage(self.driver)
        checkout=homepage.shopItems()
        log.info("Getting all the cart Titles")
        #checkout=CheckoutPage(self.driver)   
        products=checkout.getcartTitles()
        
        #confirmpage=ConfirmPage(self.driver)
        
        i=-1
        for product in products:
            i=i+1
            prodName=product.text
            log.info(prodName)
            if prodName=="Blackberry":
                #add item to cart
                #//div[@class='card h-100']/div[2]/button
                checkout.getcartFooters()[i].click()
        
        checkout.getcheckout().click()
        confirmpage=checkout.getcartcheckout()
        log.info("Entering Country Name-IND")
        confirmpage.getSearch().send_keys("Ind")
        
        self.verifyLinkPresence("India")

        #=======================================================================
        # wait=WebDriverWait(self.driver,7)
        # wait.until(expected_conditions.presence_of_element_located(confirmpage.enteredtxt))
        #=======================================================================
        confirmpage.getEnteredText().click()

        confirmpage.getCheckbox().click()
        confirmpage.getButton().click()

        print(confirmpage.getAlertText().text)
        message=confirmpage.getAlertText().text
        log.info("Text received form application is"+message)
        assert "Your order will be delivered" in message
