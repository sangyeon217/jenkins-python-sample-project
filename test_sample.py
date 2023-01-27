import random


def test_sample1(driver, web_test_logger):
    url = "https://www.google.com/"
    driver.get(url)

    web_test_logger.debug(msg="DEBUG MESSAGE")
    web_test_logger.info(msg=f"Opening {url}")
    web_test_logger.warning(msg="WARNING MESSAGE")
    web_test_logger.error(msg="ERROR MESSAGE")
    assert random.choice([True, False])
