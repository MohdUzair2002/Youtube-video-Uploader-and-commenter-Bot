from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
import time
links=[]
no_of_count=int(input("how many times you want to upload the video"))

chrome_options =webdriver.ChromeOptions()

##chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")
s=Service(ChromeDriverManager().install())
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=s,options=chrome_options)
i=0
while(i<no_of_count):
    url='https://www.youtube.com'
    chrome.get(url)
    up_butt=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//yt-icon[@class='style-scope ytd-topbar-menu-button-renderer']")))
    chrome.execute_script("arguments[0].click();", up_butt)
    upload_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='primary-text-container']")))
    chrome.execute_script("arguments[0].click();", upload_button)
    select_files=chrome.find_element( By.XPATH,"//input[@type='file']")
    select_files.send_keys("W:/Youtube VIdeo Uploader and Commenter/Video/1.mp4")
    not_for_kids=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@name='VIDEO_MADE_FOR_KIDS_NOT_MFK']")))
    chrome.execute_script("arguments[0].click();", not_for_kids)
    link=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='value style-scope ytcp-video-info']//a")))
    time.sleep(5)
    link=chrome.find_element( By.XPATH,"//div[@class='value style-scope ytcp-video-info']//a")
    print(i,link.text)
    links.append(link.text)
    next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
    chrome.execute_script("arguments[0].click();", next_button)
    next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
    chrome.execute_script("arguments[0].click();", next_button)
    try:
        next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
        chrome.execute_script("arguments[0].click();", next_button)
    except:
        next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]")))
        chrome.execute_script("arguments[0].click();", next_button)
    try:
     public=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text (),'Public')]")))
     chrome.execute_script("arguments[0].click();", public)
    except:
        next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
        chrome.execute_script("arguments[0].click();", next_button)
        public=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text (),'Public')]")))
        chrome.execute_script("arguments[0].click();", public)

    # save=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div")))
    # chrome.execute_script("arguments[0].click();", save)
    # time.sleep(10)
    i+=1
