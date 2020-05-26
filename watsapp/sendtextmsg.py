# Selenium works very good when we want to automate a task.
# Webdriver is used to connect and work with any website. 
# (running locally i.e., before hosting or already hosted on a webserver).
from selenium import webdriver
import os

# Driver is like mediator between python script and website. 
# Like "Type 4 Oracle driver" for connecting java to Oracle DB.
# Driver is used for pretty much everything we want to happen here.
# Download ChromeDriver based on the version of your chrome browser and OS.
path = os.path.dirname(os.path.realpath(__file__))
path += "/chromedriver"

# Chrome is the web browser that we use to browse.
driver = webdriver.Chrome(executable_path = path)
# for Firefox : webdriver.Firefox() --> Selenium default browser. No arguments required.
# for Internet Explorer : webdriver.Ie()
# for Edge : webdriver.Edge()
# for PhantomJS : webdriver.PhantomJS()

# get() mtd accepts the URL what we want to connect.
driver.get('https://web.whatsapp.com/')

input("Scan the QR code and hit any button !")  # Stopping the script until window loads completely.

# Taking the details of destination.
Chat_title = input("Chat Title : ")
Chat_text_msg = input("Chat Message : ")
Chat_repeat = int(input("Chat Repeat : "))

# xpath is the selenium way of finding unique element of a webpage with the help of its attributes.
user = driver.find_element_by_xpath("//span[@title = '{}']".format(Chat_title))
user.click()  
# Clicking a navigable element.

# Finding the messagebox or input field (Like in getElementByClassName JavaScript).
message_box = driver.find_elements_by_class_name("_2S1VP")

# Regular Business Logic.
for _ in range(Chat_repeat):
    message_box[1].send_keys(Chat_text_msg)
    send = driver.find_element_by_class_name('_35EW6')
    send.click()

