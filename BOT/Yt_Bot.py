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
while(i<1):
    url='https://www.youtube.com'
    chrome.get(url)
    up_butt=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//yt-icon[@class='style-scope ytd-topbar-menu-button-renderer']")))
    chrome.execute_script("arguments[0].click();", up_butt)
    upload_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='primary-text-container']")))
    chrome.execute_script("arguments[0].click();", upload_button)
    select_files=chrome.find_element( By.XPATH,"//input[@type='file']")
    select_files.send_keys("W:/Youtube VIdeo Uploader and Commenter/Videos/1.mp4")
    not_for_kids=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@name='VIDEO_MADE_FOR_KIDS_NOT_MFK']")))
    chrome.execute_script("arguments[0].click();", not_for_kids)
    link=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='value style-scope ytcp-video-info']//a")))
    time.sleep(5)
    link=chrome.find_element( By.XPATH,"//div[@class='value style-scope ytcp-video-info']//a")
    print(link.text)
    links.append(link.text)
    next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
    chrome.execute_script("arguments[0].click();", next_button)
    next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
    chrome.execute_script("arguments[0].click();", next_button)
    next_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text (),'Next')]")))
    chrome.execute_script("arguments[0].click();", next_button)
    public=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text (),'Public')]")))
    chrome.execute_script("arguments[0].click();", public)
    save=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div")))
    chrome.execute_script("arguments[0].click();", save)
# close=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//ytcp-icon-button[@id='close-icon-button']")))
# chrome.execute_script("arguments[0].click();", save)
# 5)

    print(links[i])
    url1=links[i].split("=")[-1]
    url2=url1.split('/')[-1]
    print(url2)
    # url4='https://www.youtube.com/shorts/'+url1.split('/')[-1]
    url4='https://www.youtube.com/watch?v='+url1.split('/')[-1]
    print(url4)
    time.sleep(10)
    chrome.get(url4)
    try:
        comment=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@role='textbox']")))
        chrome.execute_script("arguments[0].click();", comment)
        comment=chrome.find_element( By.XPATH,"//*[@role='textbox']")
        comment.send_keys("Islamic")
    except:       
        time.sleep(4) 
        chrome.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(5)

        chrome.find_element_by_tag_name('body').send_keys(Keys.END) 
        time.sleep(5)
        chrome.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(5)

        chrome.find_element_by_tag_name('body').send_keys(Keys.END)               
        # comment=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@role='textbox']")))
        time.sleep(4)
        comment=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@role='textbox']")))
        chrome.execute_script("arguments[0].click();", comment)

        comment=chrome.find_element( By.XPATH,"//*[@role='textbox']")
        comment.send_keys("Islamic")
    comment_submit=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='Comment']")))
    chrome.execute_script("arguments[0].click();", comment_submit)
    menu_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer/ytd-comment-renderer/div[3]/div[3]/ytd-menu-renderer/yt-icon-button/button/yt-icon")))
    menu_button=chrome.find_element(By.XPATH,"/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer/ytd-comment-renderer/div[3]/div[3]/ytd-menu-renderer/yt-icon-button/button/yt-icon")
    chrome.execute_script("arguments[0].click();", menu_button)
    pin=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Pin')]")))
    chrome.execute_script("arguments[0].click();", pin)
    pin_confirm=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//tp-yt-paper-button[@aria-label='Pin']")))
    chrome.execute_script("arguments[0].click();", pin_confirm)
    i+=1



