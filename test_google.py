import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import allure
import datetime

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    prefs = {"intl.accept_languages": "en,en_US"}
    chrome_options.add_experimental_option("prefs", prefs)
    
    service = Service("C:\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@allure.feature("Google Search")
@allure.story("Search QA Automation Tools")
def test_google_search(driver):
    with allure.step("Open Google Page"):
        driver.get("https://www.google.com")
        driver.save_screenshot("screenshots/step_1_google_page.png")
        allure.attach.file("screenshots/step_1_google_page.png", name="Step 1: Google Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Search for QA Automation Tools"):
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("QA Automation Tools")
        driver.save_screenshot("screenshots/step_2_search_keyword.png")
        allure.attach.file("screenshots/step_2_search_keyword.png", name="Step 2: Search Keyword", attachment_type=allure.attachment_type.PNG)

    with allure.step("Submit Search and Take Screenshot"):
        search_box.submit()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        driver.save_screenshot("screenshots/step_3_search_results.png")
        allure.attach.file("screenshots/step_3_search_results.png", name="Step 3: Search Results", attachment_type=allure.attachment_type.PNG)

    with allure.step("Get Top 10 QA Automation Tools"):
        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        top_tools = []
        for result in search_results[:10]:
            title = result.find_element(By.TAG_NAME, 'h3').text
            top_tools.append(title)
        allure.attach(str(top_tools), name="Top 10 QA Automation Tools", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Navigate to News tab"):
        news_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Notícias"))
        )
        news_tab.click()
        driver.save_screenshot("screenshots/step_4_news_tab.png")
        allure.attach.file("screenshots/step_4_news_tab.png", name="Step 4: News Tab", attachment_type=allure.attachment_type.PNG)

    with allure.step("Display news titles from the last 3 months"):
        tools_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Tools"]'))
        )
        tools_button.click()
        
        recent_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Recent"]'))
        )
        recent_dropdown.click()
        
        custom_range_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Custom range..."]'))
        )
        custom_range_option.click()
    
        three_months_ago = datetime.datetime.now() - datetime.timedelta(days=90)
        from_date_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@aria-label="From"]'))
        )
        from_date_field.clear()
        from_date_field.send_keys(three_months_ago.strftime("%m/%d/%Y"))
        from_date_field.send_keys(Keys.RETURN)
        
        go_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//g-button[contains(@class, "go-button-class")]'))
        )
        go_button.click()
    
        news_results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "NiLAwe")]'))
        )
        recent_news_titles = []
        three_months_ago = datetime.datetime.now() - datetime.timedelta(days=90)
        
        for news in news_results:
            date_element = news.find_element(By.TAG_NAME, 'time')
            if date_element:
                date_str = date_element.get_attribute("datetime")
                news_date = datetime.datetime.fromisoformat(date_str[:-1])
                if news_date >= three_months_ago:
                    title = news.find_element(By.TAG_NAME, 'h3').text
                    recent_news_titles.append(title)
        allure.attach(str(recent_news_titles), name="Recent News Titles", attachment_type=allure.attachment_type.TEXT)