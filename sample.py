from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from file.log import logging_config
import logging


def open_google_web():
    logging_config.init()
    web_logger = logging.getLogger(name='web')

    web_logger.debug(msg="DEBUG MESSAGE")
    web_logger.info(msg=f"INFO MESSAGE")
    web_logger.warning(msg="WARNING MESSAGE")
    web_logger.error(msg="ERROR MESSAGE")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    url = "https://www.google.com/"

    try:
        driver.get(url)
        logging_config.save_browser_logs(logger=web_logger, driver=driver, msg=f"{url}")
    finally:
        driver.quit()
