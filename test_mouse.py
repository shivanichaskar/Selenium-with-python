from selenium.webdriver import Chrome

#for performing actions
from selenium.webdriver.common.action_chains import ActionChains

#for usig keys
from selenium.webdriver.common.keys import Keys

def test_mouse():

    #for time.sleep
    import time
    path="D:\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/")
    obj = ActionChains(driver)

    #click any where where ever the control is
    #obj.click().perform()
    #to click on any specific element
    #obj.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #right click
    #obj.context_click().perform()
    #obj.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #double click
    #obj.double_click().perform()
    #obj.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #
    obj.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()

