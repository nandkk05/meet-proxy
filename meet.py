import time
import requests
import schedule
from datetime import datetime
from selenium import webdriver
from time import sleep as delay
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


url = "https://meet.google.com/lookup/fznv2tt4lr?authuser=1&hs=179";
#url = "https://meet.google.com/dtv-smii-efn"

op = Options()
op.add_argument("start-maximized")
op.add_argument("use-fake-ui-for-media-stream")
op.add_experimental_option('useAutomationExtension', False)
op.add_experimental_option("excludeSwitches", ["enable-automation"])

op.add_argument(
    '--user-data-dir=D:\\Libraries\\Desktop\\cpp-notes\\profile')

op.add_argument(
    '--profile-directory= Profile 2')

driver = webdriver.Chrome(options=op)

chat_id = '587329288'
api_key = '1323350494:AAGytCoJVO6d_Z_CTlRFmVwcFoWYdlDP9Lc'

def join_class():

    driver.get(url)

    driver.implicitly_wait(10)

    camera_button = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div').click()

    mic_button = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div').click()

    """
    Remove this from comment if you're setting up this on virtual env or Remote Desktop Connection
    
    dismiss_button = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click() 
    """


    delay(3)

    enter_meeting_button = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()

    
    def send_message():
        chat_id = '587329288'
        api_key = '1323350494:AAGytCoJVO6d_Z_CTlRFmVwcFoWYdlDP9Lc'
        
        message = 'Class joined', datetime.now().strftime('%H:%M')
        telegram_url = "https://api.telegram.org/bot{}/sendMessage?text={}&chat_id={}".format(api_key, message, chat_id)
        telegram_response = requests.get(telegram_url)

    print("CLASS JOINED SUCESSFULLY @", datetime.now().strftime('%H:%M'))

def leave_class():

    try:
        leave_button = driver.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div/div[1]').click()

        print("CLASS LEFT SUCESSFULLY @", datetime.now().strftime('%H:%M'))

    except NoSuchElementException:
        print("YOU WERE KICKED OUT BEFORE TIME")

    #driver.close()

#1st Class
schedule.every().day.at("16:45").do(join_class)
schedule.every().day.at("09:49").do(leave_class)

#2nd Class
if(datetime.now().strftime('%A') != 'Friday'):
    schedule.every().day.at("10:00").do(join_class)
    schedule.every().day.at("10:49").do(leave_class)

#3rd Class
schedule.every().day.at("11:00").do(join_class)
schedule.every().day.at("11:49").do(leave_class)

#4th Class
if(datetime.now().strftime('%A') != 'Monday'):
    schedule.every().day.at("12:00").do(join_class)
    schedule.every().day.at("12:49").do(leave_class)

while True:
    schedule.run_pending()
    time.sleep(30)