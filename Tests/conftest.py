'''
Created on 25 Sep 2020

@author: 611104661
'''
import pytest
from selenium import webdriver
driver = None


#to activate CMD arguments
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="Chrome")


@pytest.fixture(scope="class")
def setup(request):
    #setting Global driver
    global driver
    #providing driver details
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver=webdriver.Chrome(executable_path="C:\Selenium Java\BrowserDrivers\chromedriver_win32\chromedriver.exe")       
    elif browser_name=="firefox":
        driver=webdriver.Firefox(executable_path="C:\Selenium Java\BrowserDrivers\geckodriver-v0.27.0-win64\geckodriver.exe")      
    elif browser_name=="ie":
        driver=webdriver.Ie(executable_path="C:\Selenium Java\BrowserDrivers\IEDriverServer_x64\IEDriverServer.exe")      
    else:
        driver=webdriver.Chrome(executable_path="C:\Selenium Java\BrowserDrivers\chromedriver_win32\chromedriver.exe")
        
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #method to handle driver if present in two files
    request.cls.driver=driver
    yield
    driver.close()
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

def _capture_screenshotAB(name):
        driver.get_screenshot_as_file(name)