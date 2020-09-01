
# coding: utf-8

# In[3]:




import time
from selenium import webdriver

url='https://www.hudl.com/'

class hudllogin(object):
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
        self.driver.get(url)
        
        
     
    def login(self):
        linkText=self.driver.find_element_by_link_text("Log in")
        time.sleep(1)
        linkText.click()

# To maintain the security of user credentials program read id and password from Text file.        
        
        email = self.driver.find_element_by_id("email")
        
        with open('Eid.txt', 'r') as myfile:
            eid = myfile.read().replace('\n', '')
       
        email.send_keys(eid)

        Password = self.driver.find_element_by_id("password")
        #password.send_keys("sourabh@12")
        
        with open('password.txt', 'r') as myfile:
            password = myfile.read().replace('\n', '')
            
        Password.send_keys(password)

        time.sleep(1)

        login = self.driver.find_element_by_id("logIn")
        login.click()
        
        time.sleep(2)
        
# Below fnction is created to claim Live game or Training game according to their availability.

    def request_start(self):    
        
        
        
        available_live = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/h3").text
        
        live =available_live.split(" ")
        
#If 0 Live games are available on dashboard then it automatically goes is Training tab and claim training game of volleyball.       
        
        if int(live[1]) == 0:
            
            training =self.driver.find_element_by_link_text("Training")
            training.click()

            time.sleep(1)
            
            volleyball =self.driver.find_element_by_link_text("Volleyball")
            volleyball.click()
        
            time.sleep(1)
        
            available = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/h3").text
        
            s1=available.split(" ")
            
            if int(s1[1]) > 1900:
                self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/button").click()
            
                time.sleep(2)
            
                self.driver.find_element_by_xpath("//*[@id='assigned-job-pane']/div[3]/div/div[2]/button").click()
            
        
                time.sleep(2)
        
        else:
            
            print("Request Live Game")
            self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/button").click()
            
        #self.driver.close()
        
        
h1=hudllogin()
h1.login()
h1.request_start()

