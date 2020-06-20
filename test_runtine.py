#chrome is a browser object
from selenium.webdriver import Chrome

#this import is used for dropdown or list function
from selenium.webdriver.support.select import Select

def test_runtime():

    #chromedriver link
    path="D:\\chromedriver_win32\\chromedriver.exe"

    #object of browser object
    driver = Chrome(executable_path=path)

    #passing url
    driver.get("http://www.theTestingWorld.com/testings")

    #max browser
    driver.maximize_window()

    #fetch the title
    #print(driver.title)

    #fetch url
    #print(driver.current_url)

    #fetch page source
    #print("-**")
    #print(driver.page_source)


    #fetching element text
    print("text on link is    " + driver.find_element_by_class_name("displayPopup").text)

    #fetching attribute
    print("value of button     " + driver.find_element_by_xpath("//input[@type='submit']").get_attribute("value"))