
###############################
# Remarks
###############################
# Module for AU Jibun Bank login

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
# AUjibun_bank_login
###############################
def AUjibun_bank_login(driver,wait, username,password):
    try:
        # shadow-rootの非表示（必要になれば利用）
        '''
        script = """
        document.querySelectorAll('*').forEach(el => {
            if (el.shadowRoot) {
                el.style.display = 'none';
                console.log('Hidden shadow host:', el);
            }
        });
        """
        driver.execute_script(script)
        '''
        logger.info('Enter your login information.')
        driver.find_element(By.NAME, 'customerNo').clear()
        driver.find_element(By.NAME, 'loginPW').clear()
        driver.find_element(By.NAME, 'customerNo').send_keys(username)
        driver.find_element(By.NAME, 'loginPW').send_keys(password)
        driver.find_element(By.CLASS_NAME, "c-btn-main.is-large.is-w474.is-icon-arrow-next.js-validate-submit").click()
        logger.info('Clicked on the login button.')
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/div[1]/div[1]/div/ul/li[1]/p")))
    except Exception as e:
        logger.error ('login failed.')
        logger.error ('=== Error Content ===')
        logger.error ('type:' + str(type(e)))
        logger.error ('args:' + str(e.args))
        logger.error ('e:' + str(e))
        raise
    else:
        logger.info('Login completed.')

