import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.keys import Keys
from loguru import logger
from .models import Account


def main(username):
    log_output = ""  
    logger.info("Запускаю эмуляцию!")
    log_output += "Запускаю эмуляцию!\n"
    account = Account.objects.first()
    driver = webdriver.Chrome()
    driver.get("https://ru.stripchat.global/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Мне больше 18 лет']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/header/div/div/nav[2]/div[2]/a[4]').click()
    time.sleep(10)

    if account:

        logger.success(f"Аккаунт найден - {account.email}:{account.password}")
        driver.find_element(By.ID, 'login_login_or_email').send_keys(account.email)
        driver.find_element(By.ID, 'login_password').send_keys(account.password)
    else:
        log_output += "Нет доступных аккаунтов в базе данных.\n"  

    api_key = '9fe3a62e9d89f6d358dbaa3facc553c7'
    solver = TwoCaptcha(api_key)
    response = solver.recaptcha(sitekey='6LdERdoaAAAAAD5YwFuKYsGz6VWgo6tC2ZMtQVmg', url="https://ru.stripchat.global/")
    logger.info('Капча решена: ' + str(response))
    recaptcha_response = response["code"]

    symbols = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for symbol in symbols:
        try:
            resp = driver.execute_script(f"return ___grecaptcha_cfg.clients['0']['{symbol}']['{symbol}']")
            if 'callback' in resp:
                driver.execute_script(
                    f"___grecaptcha_cfg.clients['0']['{symbol}']['{symbol}']['callback']('{recaptcha_response}')")
                logger.success(f"Сегодня буква {symbol}")
                log_output += f"Сегодня буква {symbol}\n"  
                break
        except Exception:
            pass

    driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div[1]/div/div[2]/div/form/div[4]/button').click()
    logger.success("Успешно зашел на аккаунт")
    log_output += "Успешно зашел на аккаунт\n"  
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/div[3]/div[2]/nav[2]/div').click()
    username_input = driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/div[3]/div[2]/nav[2]/div/div/div[1]/input')
    username_input.send_keys(username)
    username_input.send_keys(Keys.ENTER)
    logger.info(f"Зашел на аккаунт {username}")
    log_output += f"Зашел на аккаунт {username}\n"  
    time.sleep(20)
    driver.quit()

    return log_output  
