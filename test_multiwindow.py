from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By

@pytest.fixture()
def environment_setup():

    global driver
    path = "D:\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    yield
    driver.close()

def test_verift_reg(environment_setup):
   driver.find_element_by_xpath("//label[text()='Login']").click()
   driver.find_element_by_name("_txtUserName").send_keys("test")
   driver.find_element_by_name("_txtPassword").send_keys("test")
   driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
   driver.find_element_by_xpath("//a[contains(text(),' My Account')]").click()
   driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()
   time.sleep(10)
   allwindow = driver.window_handles
   #print(allwindow)
   mainwin=''

   for win in allwindow:
       driver.switch_to.window(win)
       #print(driver.current_url)
       if(driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
           driver.find_element_by_xpath("//button[text()='Start Download']").click()
           time.sleep(5)
           driver.close()
       elif(driver.current_url=='https://www.thetestingworld.com/testings/dashboard.php'):
            mainwin=win

   driver.switch_to.window(mainwin)
   print(driver.current_url)



