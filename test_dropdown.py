#chrome is a browser object
from selenium.webdriver import Chrome

#this import is used for dropdown or list function
from selenium.webdriver.support.select import Select
import pytest
import time

#for explicit wait
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

from selenium.webdriver.common.by import By

@pytest.fixture()
def environment_setup():

    global driver
    # chromedriver link
    path = "D:\\chromedriver_win32\\chromedriver.exe"

    # object of browser object
    driver = Chrome(executable_path=path)
    #driver.set_page_load_timeout(10)
    # passing url
    driver.get("http://www.theTestingWorld.com/testings")

    # implecitly wait
    driver.implicitly_wait(10)
        # max browser
    driver.maximize_window()

#will execute after test case
    yield
    # close browser
    driver.close()

def test_verift_reg(environment_setup):
    # create obj of wait
    wait = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element(By.ID,'countryId'),"India")
    # radio button
    # driver.find_element_by_xpath("//input[@value='home']").click()
    #driver.find_element_by_xpath("//input[@value='office']").click()

    #dropdown
    obj = Select(driver.find_element_by_id("countryId"))
    obj.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element(By.ID, 'stateId'), "Goa")

    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Goa")
    #index approch
    #obj.select_by_index(1)
    #select by value approch
    #obj.select_by_value("2")

    #fetch selected data and
    #print(obj.first_selected_option.text)

    #fetch all the data in the list
    #for op in obj.options:
     #   print(op.text)


    # dropdown(can select only one option)
    #obj = Select(driver.find_element_by_name("sex"))
    # index approch
    # obj.select_by_index(1)
    # select by value approch
    # obj.select_by_value("2")

    # by visible text
    #obj.select_by_visible_text("Male")

    #wait add force wait
    #time.sleep(10)


    # check box
    #driver.find_element_by_name("terms").click()
    # driver.find_element_by_xpath("//input[@name='terms']").click()

    # sinup button iporthatnt field
    # driver.find_element_by_xpath("//input[@value='Sign up']").click()

    #button
   # driver.find_element_by_xpath("//input[@type='submit']").click()

    # link
    #driver.find_element_by_link_text("Read Detail").click()
    #assert driver.current_url == "https://www.thetestingworld.com/testings/"

