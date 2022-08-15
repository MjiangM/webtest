from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 老版本python和selenium是这样写的的驱动浏览器：driver = webdriver.Chrome("./chromedriver.exe")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 隐藏正在受到自动化测试软件的控制这句话
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',
                                       ['enable-automation'])
service = Service("../../chromedriver.exe")
driver = webdriver.Chrome(service=service,options=chrome_options)

driver.maximize_window()


driver.get("https://www.jd.com")
# driver.find_element(by=By.CSS_SELECTOR,value="#key").send_keys("电脑")
# driver.find_element(by=By.CSS_SELECTOR,
#                     value="#search > div > div.form > button").click()
jiadian_element = driver.find_element(by=By.CSS_SELECTOR,value="#J_cate ul li:nth-child(1) a")
# 鼠标悬停
ActionChains(driver).move_to_element(jiadian_element).perform()
time.sleep(2)
#定位全面屏电视
tv = driver.find_element(by=By.CSS_SELECTOR,value="#cate_item1 > div.cate_part_col1 > div.cate_detail > dl.cate_detail_item.cate_detail_item1 > dd > a:nth-child(1)")
tv.click()

handlers = driver.window_handles
# 2.迭代当前句柄
for h in handlers:
    # 如果h不等于当前的handlers
    if h!= driver.current_window_handle:
#         切换到这个句柄上
        driver.switch_to.window(h)
    print("当前句柄是："+driver.title)

driver.find_element(by=By.CSS_SELECTOR,value="[title=小米（MI）]").click()