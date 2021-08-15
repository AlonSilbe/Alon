from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#site usedto find number info
url = 'https://441il.com/'
#file with numbers to put in site
file = open(r"C:\Users\Alon1000\Desktop\numbers.txt", "r")
#read each numbner
num1= file.readline()
num2= file.readline()
file.close()

#input number
#file with numbers to put in site
file = open(r"C:\Users\Alon1000\Desktop\numbers.txt", "r")
#read each numbner
num1= file.readline()
num2= file.readline()
#close file
file.close()

#function for finding number info in the site
def numInfo(url,num1):
    #open chrome with web driver. Driver can be downloaded at: https://chromedriver.chromium.org/downloads
    driver=webdriver.Chrome(executable_path=r"C:\Users\Alon1000\Desktop\chromedriver.exe")
    #open site
    driver.get(url)
    #input number into site
    input=driver.find_element(By.ID,'idphone').send_keys(num1)
    #click search
    driver.find_element(By.ID,'idsearch').click()
    time.sleep(4)
    #read the each column in the resulting table with the info
    results=driver.find_elements_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[1]")
    for value in results:
        print("name=", value.text)
    results=driver.find_elements_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[2]")
    for value in results:
        print("adress=", value.text)
    results=driver.find_elements_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[3]")
    for value in results:
        print("phone=", value.text)
    driver.quit()


print("Results for the first number in the document:")
numInfo(url,num1)
print("Results for the seconed number in the document:")
numInfo(url,num2)