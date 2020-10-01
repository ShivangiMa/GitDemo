'''
Created on 25 Sep 2020

@author: 611104661
'''
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging
import inspect


@pytest.mark.usefixtures("setup")
class BaseClassA:

    def test_getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)

        filehandler=logging.FileHandler("logfile.log")

        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        #logger.setLevel(logging.CRITICAL)
        return logger
           
           
    def verifyLinkPresence(self,text):    
        wait=WebDriverWait(self.driver,7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))
        
        
    def selectOptionbyVisibleText(self,locator,text):
        sel=Select(locator)
        sel.select_by_visible_text(text)