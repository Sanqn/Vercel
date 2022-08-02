import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")


def news_pars():
    link = f'https://tlgrm.ru/channels/@showtimeinfo'
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(link)
    time.sleep(1)
    # for i in range(4):
    #     botton_next = browser.find_element(By.CLASS_NAME, "cfeed-loadmore-tear__button")
    #     browser.execute_script("return arguments[0].scrollIntoView(true);", botton_next)
    #     botton_next.click()
    #     time.sleep(1)
    time_create_post = browser.find_elements(By.XPATH, '//div[@channel_id="1143557060"]/header/section/footer/time')
    title_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text > b")
    dick_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text")
    return time_create_post, title_post, dick_post


data_time = {'час назад': 60, '2 часа назад': 120,
             '3 часа назад': 180, '4 часа назад': 240,
             '5 часов назад': 300, '6 часов назад': 360,
             '7 часов назад': 420, '8 часов назад': 480,
             '9 часов назад': 540, '10 часов назад': 600,
             '11 часов назад': 660, '12 часов назад': 720,
             '13 часов назад': 780, '14 часов назад': 840,
             '15 часов назад': 900, '16 часов назад': 960,
             '17 часов назад': 1020, '18 часов назад': 1080,
             '19 часов назад': 1140, '20 часов назад': 1200,
             '21 час назад': 1260, '22 часа назад': 1320,
             '23 часа назад': 1380, '24 часа назад': 1440,
             '1 день назад': 1441,
             'вчера': 1441, '2 дня назад': 2881,
             '3 дня назад': 4021, '4 дня назад': 5461,
             '5 дней назад': 6901, '6 дней назад': 8341,
             'неделю назад': 10080, '2 недели назад': 20160,
             '3 недели назад': 30240, '4 недели назад': 40320,
             }
