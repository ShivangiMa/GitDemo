'''
Created on 25 Sep 2020

@author: 611104661
'''
from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import ConfirmPage


class CheckoutPage :

    def __init__(self,driver):
        self.driver=driver
    
    #Defining Page objects
    cartTitle=(By.XPATH,"//div[@class='card h-100']/div/h4/a" )
    cartFooter=(By.CSS_SELECTOR,".card-footer button" )
    checkout=(By.PARTIAL_LINK_TEXT,"Checkout" )
    cartcheckout=(By.XPATH,"//button[@class='btn btn-success']" )
    
    # Methods to invoke
    def getcartTitles(self):
        return self.driver.find_elements(*CheckoutPage.cartTitle)
    
    def getcartFooters(self):
        return self.driver.find_elements(*CheckoutPage.cartFooter)
    
    def getcheckout(self):
        return self.driver.find_element(*CheckoutPage.checkout)
    
    def getcartcheckout(self):
        self.driver.find_element(*CheckoutPage.cartcheckout).click()
        confirmpage=ConfirmPage(self.driver)
        return confirmpage
    