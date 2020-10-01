'''
Created on 25 Sep 2020

@author: 611104661
'''
from selenium.webdriver.common.by import By
from PageObject.CheckoutPage import CheckoutPage


class HomePage :
    
    def __init__(self,driver):
        self.driver=driver
    
    #Defining Page objects
    shop=(By.CSS_SELECTOR,"a[href*='shop']" )
    name=(By.CSS_SELECTOR,"input[name='name']" )
    emailID=(By.NAME,"email")
    Password=(By.ID,"exampleInputPassword1" )
    checkme=(By.ID,"exampleCheck1" )
    gender=(By.ID,"exampleFormControlSelect1")
    status=(By.XPATH,"//input[@id='inlineRadio2']" )
    dob=(By.NAME,"bday" )
    button=(By.CSS_SELECTOR,"input[class*='btn-success']" )
    alertmsg=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']" )


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout=CheckoutPage(self.driver)
        return checkout
    
    def getname(self):
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.emailID)
    
    def getPassword(self):
        return self.driver.find_element(*HomePage.Password)
    
    def getCheckMe(self):
        return self.driver.find_element(*HomePage.checkme)
    
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    
    def getStatus(self):
        return self.driver.find_element(*HomePage.status)
    
    def getDateofBirth(self):
        return self.driver.find_element(*HomePage.dob)
    
    def getSubmit(self):
        return self.driver.find_element(*HomePage.button)
    
    def getAlertMsg(self):
        return self.driver.find_element(*HomePage.alertmsg)

    def getAlertABCD(self):
        return self.driver.find_element(*HomePage.alertmsg)

    