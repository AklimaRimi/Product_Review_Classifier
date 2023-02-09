from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import time 

driver = webdriver.Chrome()
driver.get(r'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011&qid=1675150266&ref=sr_pg_1')

data = []
for page in range(1,91):   
    print(page) 
    lists = driver.find_elements(By.XPATH,"//div[contains(@class,'a-section') and contains(@class,'a-spacing-none') and contains(@class,'a-spacing-top-small') and contains(@class,'s-title-instructions-style')]")

    for list in lists:
        name = list.find_element(By.TAG_NAME,'h2').text
        link = list.find_element(By.TAG_NAME,'a').get_attribute('href')      

        data.append([name,link])
    
    next = driver.find_element(By.XPATH,"//a[contains(@class,'s-pagination-item') and contains(@class,'s-pagination-next') and contains(@class,'s-pagination-button') and contains(@class,'s-pagination-separator')]")
    actions = ActionChains(driver)
    actions.click(next)
    actions.perform()
    time.sleep(2)

df = pd.DataFrame(data,columns=['Name','Link'])
df.to_csv('toy-product-info.csv',index=False)