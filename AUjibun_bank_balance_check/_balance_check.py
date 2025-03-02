
###############################
# Remarks
###############################
# Module for balance check

###############################
# Import
###############################
import logging
from AUjibun_bank_balance_check import _setup_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Use common log settings
logger = logging.getLogger(__name__)

###############################
# AUjibun_bank_balance_check
###############################
def balance_check(driver,wait, username,password):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/div[1]/div[1]/div/ul/li[1]/p")))
        balance = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/div[1]/div[1]/div/ul/li[1]/p")
        logger.info(balance.text)#1,889,243円
        return balance.text
    except Exception as e:
        logger.error  ("Balance check failed")
        logger.error ('=== Error Content ===')
        logger.error ('type:' + str(type(e)))
        logger.error ('args:' + str(e.args))
        logger.error ('e:' + str(e))
        raise

