"""
  ____                                                        
 / ___| _ __   __ _ _ __ ___  _ __ ___   ___  _   _  ___ _ __ 
 \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \| | | |/ _ \ '__|
  ___) | |_) | (_| | | | | | | | | | | | (_) | |_| |  __/ |   
 |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___/ \__, |\___|_|   
       |_|                                    |___/           

"""
# A simple whatsapp spammer written in python using
# selenium webdriver. Have fun! by Zagnox

from selenium import webdriver
from selenium.webdriver.common.by import By
from ascii import artwork

print(artwork)
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Vendos emrin e userit ose grupit: ')
msg = input('Vendos mesazhin spam ketu: ')
numri = int(input('Vendos numrin e spameve (p.sh. 1000): '))

input('Skano kodin QR dhe shtyp enter')

user = driver.find_element(By.XPATH, f'//span[@title = "{name}"]')
user.click()

msg_box = driver.find_element(By.CLASS_NAME, '_3Uu1_')

for i in range(numri):
    msg_box.send_keys(msg)
    button = driver.find_element(By.CLASS_NAME, '_3XKXx')
    button.click()
