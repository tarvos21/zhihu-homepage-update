#coding:utf-8

# python2 runs Ok, it needs some modification for python3
# python3 supports Selenium better

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# path to chromedriver
driver = webdriver.Chrome('/home/bing/Downloads/chromedriver')

# login from signin page
driver.get('https://www.zhihu.com#signin')
name = driver.find_element_by_name('account')
passwd = driver.find_element_by_name('password')
name.send_keys('phone number/email address')
time.sleep(0.5)
passwd.send_keys('password')
time.sleep(0.5)
submit = driver.find_element_by_tag_name('button')
submit.click()

# iterate n times to kill items
i = 0
total_item = 0
total_page = 0
error = 0
while(i < 100):
    # wait until the elements appear on the page
    try:
        check = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.NAME, 'dislike')))
        num = check.__len__()

        # kill all the items in current page
        for i in range(num):
            
            dislike = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.NAME, 'dislike')))
            dislike.click()

            time.sleep(0.8)

            # close the notice message in one line
            close = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'close')))
            close.click()

            time.sleep(0.8)


            total_item += 1

        # click "more" button twice
        more = driver.find_element_by_id("zh-load-more")
        more.click()
        time.sleep(2)
        more = driver.find_element_by_id("zh-load-more")
        more.click()
        time.sleep(1)
        total_page += 1

        print("Kill items: %d Kill pages: %d" % (total_item, total_page))

    # sometimes clicking on the "more" button response nothing
    # so try to refresh the whole page
    except:
        print "Errors happens, refresh..."
        driver.refresh()
        print "Refreshed, waiting..."
        time.sleep(5)
        driver.execute_script("scroll(0, -250);")
        print "5s end, go back to start"
        error += 1
        print("Error times: %d" % error)

    i += 1
