from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="/home/marek/Desktop/git/ucimeshardverom-website/chromedriver")
action = ActionChains(driver)

driver.get("https://makecode.microbit.org/_33CK1RgD5iw7")
driver.find_element_by_css_selector('.ui.tiny.button').click()

sleep(5)
# source = driver.find_element_by_css_selector('.blocklyBlockCanvas')
# action.context_click(source)
# action.perform()



# scrollbar = driver.find_element_by_css_selector('.blocklyScrollbarVertical.blocklyMainWorkspaceScrollbar')
# action.move_to_element_with_offset(scrollbar, -5, 5)

# action.context_click()
# action.perform()

# driver.sendKeys(Keys.UP);
