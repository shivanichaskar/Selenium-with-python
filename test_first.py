#chrome is a browser object
from selenium.webdriver import Chrome

#this import is used for dropdown or list function
from selenium.webdriver.support.select import Select

def test_first():

    #chromedriver link
    path="D:\\chromedriver_win32\\chromedriver.exe"

    #object of browser object
    driver = Chrome(executable_path=path)

    #passing url
    driver.get("http://www.theTestingWorld.com/testings")

    #max browser
    driver.maximize_window()

    #work on text box
    #enter data
    driver.find_element_by_name("fld_username").send_keys("helloworld")
    driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("abcd@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("helloo")
    driver.find_element_by_name("fld_cpassword").send_keys("helloo")
    driver.find_element_by_name("fld_username").clear()
    driver.find_element_by_name("fld_username").send_keys("worldhello")

#radio button
#driver.find_element_by_xpath("//input[@value='home']").click()
#driver.find_element_by_xpath("//input[@value='office']").click()

#dropdown(can select only one option)
#obj = Select(driver.find_element_by_name("sex"))
#index approch
#obj.select_by_index(1)
#select by value approch
#obj.select_by_value("2")

#by visible text
#obj.select_by_visible_text("Male")

#deselect options are used for only list

#check box
#driver.find_element_by_name("terms").click()
#driver.find_element_by_xpath("//input[@name='terms']").click()

#sinup button iporthatnt field
#driver.find_element_by_xpath("//input[@value='Sign up']").click()

#link
#driver.find_element_by_link_text("Read Detail").click()

#close browser
#driver.close()



