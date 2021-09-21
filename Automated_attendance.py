

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

ids = {"googleaccountname@blah.com":"YesthisismyrealPa$$word" 
        }

for username, password in ids.items():

    try:
        driver.get("https://lms-practice-school.bits-pilani.ac.in/mod/attendance/view.php?id=2669&view=5")
        print(driver.title)

        #Click on Google signin button

        driver.find_element_by_xpath("//*[@id='region-main']/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a").click()

        driver.implicitly_wait(2)

        #Enter email id

        driver.find_element_by_name("identifier").send_keys(username)
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()

        driver.implicitly_wait(2)

        #Enter password

        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span").click()

        driver.implicitly_wait(2)

        #Locate and click on submit attendance link

        for i in range(69):
            try:
                driver.find_element_by_xpath("//*[@id='region-main']/div[1]/table[1]/tbody/tr["+ str(i) +"]/td[3]/a").click()
                driver.implicitly_wait(2)
                break
            except:
                print(i)

        #Click on 'present' option

        driver.find_element_by_xpath("//*[@id='fgroup_id_statusarray']/div[2]/fieldset/div/label[1]/span").click()

        driver.implicitly_wait(2)

        driver.find_element_by_xpath("//*[@id='id_submitbutton']").click()

        driver.implicitly_wait(2)

        time.sleep(10)
        print("Attendance marked successfully :)")
        driver.close()
    except:
        print(username)
