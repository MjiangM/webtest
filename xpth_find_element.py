# xpth学习网址：https://www.w3school.com.cn/xpath/index.asp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 老版本python和selenium是这样写的的驱动浏览器：driver = webdriver.Chrome("./chromedriver.exe")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 跳转到最新的页面函数,传参用的是不定长参数(加一个*为不定长的参数)
def to_new_handler(driver,*have_handlers):
    handlers = driver.window_handles
    for h in handlers:
        if h not in have_handlers:
            driver.switch_to.window(h)
    return driver
# 隐藏正在受到自动化测试软件的控制这句话
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',
                                       ['enable-automation'])
service = Service("../../chromedriver.exe")
driver = webdriver.Chrome(service=service,options=chrome_options)

driver.maximize_window()
driver.get("https://www.jd.com")

driver.find_element(by=By.XPATH,value="//*[@id=\"J_cate\"]/ul/li[1]/a").click()

index_page_handler = driver.current_window_handle
to_new_handler(driver,index_page_handler)
# handlers = driver.window_handles
# for h in handlers:
#     if h != index_page_handler:
#         driver.switch_to.window(h)
print("当前页面是："+ driver.title)

jiadian_handler = driver.current_window_handle
driver.find_element(by=By.XPATH,value="//*[@id=\"app\"]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/ul/li[1]/a").click()

to_new_handler(driver,index_page_handler,jiadian_handler)
# handlers = driver.window_handles
# for h in handlers:
#     if h != index_page_handler and h != jiadian_handler :
#         driver.switch_to.window(h)
print("当前页面是："+ driver.title)

TV_handler = driver.current_window_handle
# 页面滚动,执行js，向左右滚动0，向上下滚动600像素
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)
driver.find_element(by=By.XPATH,value="//*[@id=\"app\"]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div").click()

to_new_handler(driver,index_page_handler,jiadian_handler,TV_handler)
# handlers = driver.window_handles
# for h in handlers:
#     if h != index_page_handler and h != jiadian_handler and h != TV_handler :
#         driver.switch_to.window(h)
print("当前页面是："+ driver.title)

# 关闭当前页面
driver.close()
# 切换页面后关闭
driver.switch_to.window(TV_handler)
driver.close()

time.sleep(2)
# 退出浏览器
driver.quit()