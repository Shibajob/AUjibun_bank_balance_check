"""Main module."""

###############################
# Remarks
###############################
# Module for creating and deleting folders for user profiles

###############################
# Import
###############################
import os
import logging
from AUjibun_bank_balance_check import _setup_logger
from AUjibun_bank_balance_check import _userprofilefolder as userprofilefolder
from AUjibun_bank_balance_check import _login as login
from AUjibun_bank_balance_check import _balance_check as balance_check
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Use common log settings
logger = logging.getLogger(__name__)

###############################
# Parameters
###############################
MAX_RETRIES = 3

CURRENT_DIR_PATH = os.path.dirname(__file__)
USER_PROFILE_PATH = CURRENT_DIR_PATH + r'\userdata'
DRIVER_PATH = CURRENT_DIR_PATH + r'\driver'
URLPATH = 'https://ib.jibunbank.co.jp/security/ap/loginlogout/login/loginstart?cid='

#Chrome Options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--no-sandbox')
options.add_argument('--lang=ja')
options.add_argument('--user-data-dir=' + USER_PROFILE_PATH)
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--start-maximized')
#options.add_argument('--headless')
options.add_argument("--disable-popup-blocking")  

###############################
# Termination process
###############################
def Process_Exit(flag):
    # User profile folder deletion process
    userprofilefolder.userprofilefolder_remove(USER_PROFILE_PATH)

    if(flag == 'true'):
        logger.info ('successful termination')
        return
    else:
        logger.error ('abnormal termination')
        raise('abnormal termination')

###############################
# Main
###############################
def AUjibun_bank_balance_check(username, passwd):
    logger.info ('===Start===')
    # If the username or password value is invalid, the process will terminate.
    if username is None or passwd is None or str(username).strip() == "" or str(passwd).strip() == "":
        logger.error ('The username or password value is invalid.')
        Process_Exit('fail')
    userprofilefolder.userprofilefolder_create(USER_PROFILE_PATH)

    # Chrome Start
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.get(URLPATH)
        logger.info ('Chrome Start')
    except Exception as e:
            logger.error ('Chrome fails to start')
            logger.error ('=== Error Content ===')
            logger.error ('type:' + str(type(e)))
            logger.error ('args:' + str(e.args))
            logger.error ('e:' + str(e))
            Process_Exit('fail')

    # Web page transition timeout
    wait = WebDriverWait(driver, 5)

    try:
        login.AUjibun_bank_login(driver, wait, username, passwd)
    except Exception:
        driver.quit()
        Process_Exit('fail')

    try:
        balance = balance_check.balance_check(driver, wait, username, passwd)
        logger.info(balance)
        return balance
    except Exception:
        driver.quit()
        Process_Exit('fail')

    driver.quit()
    Process_Exit('true')
    
