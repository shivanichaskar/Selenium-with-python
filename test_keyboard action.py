from selenium.webdriver import Chrome

#for performing actions
from selenium.webdriver.common.action_chains import ActionChains

#for usig keys
from selenium.webdriver.common.keys import Keys

def test_keybore():
    #for time.sleep
    #import time
    path="D:\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.find_element_by_name("fld_username").send_keys("hello")

    #create actionchains obj and put driver link
    obj = ActionChains(driver)

    #to perform tab operation
    #obj.send_keys(Keys.TAB).perform()

    #to perform select all
    obj.key_down(Keys.CONTROL).send_keys('a').perform()

    #preform ctr alt del
    #obj.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()

    #to give time delay
    #time.sleep(10)