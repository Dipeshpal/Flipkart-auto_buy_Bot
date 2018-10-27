from selenium import webdriver
from config import keys
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

# will cookies improve load time?
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=www.flipkart.com')

@timeme
def order(k):
    # Get product URL
    driver.get(k['product_url'])
    
    # Click on Buy Now
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[2]/form/button').click()

    time.sleep(0.5)
    
    # fill out Email/Mobile Number (Login/SignUp) screen fields
    # Enter Email/Mobile
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input').send_keys(k['email'])
    # Click on Continue
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/button').click()

    time.sleep(0.5)
   
    # Enter Password
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/input').send_keys(k['password'])
    
    # Click on Login
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[3]/button').click()


if __name__ == '__main__':
    # load chrome
    driver = webdriver.Chrome('./chromedriver')
    order(keys)
