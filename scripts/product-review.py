from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

df = pd.read_csv('toy-product-info.csv')
links = df['Link'].values

driver = webdriver.Chrome()
data = []
j =    1
for link in links:
    print(j)
    j+=1
    driver.get(link)
    try:
        product = driver.find_element(By.ID,'productTitle').text
        review_section = driver.find_element(By.XPATH,"//div[contains(@class,'a-expander-content') and contains(@class,'reviewText') and contains(@class,'review-text-content') and contains(@class,'a-expander-partial-collapse-content')]")
        review = review_section.find_element(By.TAG_NAME,'span').text
        
        data.append([product,review])
    except:
        continue
    

df = pd.DataFrame(data=data,columns=['Product','Review'])
df.to_csv('laptop-product-review.csv',index=False)

driver.close()