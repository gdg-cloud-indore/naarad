pip install selenium     # INStalling selenium
from selenium import webdriver   
driver = webdriver.Chrome()           # starting webdriver(web automation framework)
def site_login():                       #defining function for login
    driver.get("URL")
    username = driver.find_element_by_id("ID").send_keys("username")
    password = driver.find_element_by_id("ID").send_keys("password")
    driver.find_element_by_id("submit").click()
    continue = driver.find_element_by_name('continue')

    from selenium.webdriver.support import expected_condition as EC  # wait for 10 sec to find home button
    from selenium.webdriver.common.by import by
    from selenium.webdriver.support.ui import WebDriverWait WebDriverWait(driver , 10).until(EC.title_contains("home"))

