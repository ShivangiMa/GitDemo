'''
Created on 25 Sep 2020

@author: 611104661
'''
from selenium.webdriver.common.by import By


class ConfirmPage :

    def __init__(self, driver):
        self.driver=driver

    #Defining Page objects
    search=(By.CSS_SELECTOR,"input[id='country']" )
    enteredtxt=(By.LINK_TEXT,"India")
    checkbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    button=(By.CSS_SELECTOR,"input[type='submit']")
    alerttxt=(By.CLASS_NAME,"alert-success")
    

    def getSearch(self):
        return self.driver.find_element(*ConfirmPage.search)
    
    def getEnteredText(self):
        return self.driver.find_element(*ConfirmPage.enteredtxt)
    
    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    
    def getButton(self):
        return self.driver.find_element(*ConfirmPage.button)
    
    def getAlertText(self):
        return self.driver.find_element(*ConfirmPage.alerttxt)

    def getAlertTextABCD(self):
        return self.driver.find_element(*ConfirmPage.alerttxt)

    def getAlertTextEFGH(self):
        return self.driver.find_element(*ConfirmPage.alerttxt)

    def getAlertTextIJKL(self):
        return self.driver.find_element(*ConfirmPage.alerttxt)