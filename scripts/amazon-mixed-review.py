from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
import time


path = 'https://www.amazon.com/LUXSWAY-Wireless-Operated-Rotatable-Diplomas-Gold/product-reviews/B07NVZ5657/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=critical'

driver = webdriver.Chrome()
data = []

for page in range(1,45):
    driver.get(path)       

    try:
        text = driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-base review-text review-text-content')]")
        for i in text:
            print(i.text)
            data.append([i.text,0])
    
        path = driver.find_element(By.XPATH,"//li[contains(@class,'a-last')]").find_element(By.TAG_NAME,'a').get_attribute('href')
    except:
        continue

df = pd.DataFrame(data,columns=['Review','Label'])
df.to_csv('amazon_light_review2.csv',index=False)
driver.close()