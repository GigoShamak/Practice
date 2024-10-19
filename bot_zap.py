from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = 'C:\Users\iago2\Desktop\Selenium/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://web.whatsapp.com')

print("Please scan the QR code from WhatsApp Web.")
time.sleep(15)


def send_message(contact, message):
    try:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f'Message sent to {contact}: {message}')
    except Exception as e:
        print(f'Error sending message: {e}')


send_message('Contact Name', 'Hello! This is an automated message.')

time.sleep(10)
driver.quit()
