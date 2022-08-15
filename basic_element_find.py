from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 老版本python和selenium是这样写的的驱动浏览器：driver = webdriver.Chrome("./chromedriver.exe")
from selenium.webdriver.common.by import By
# 新版本写法
# service = Service("../../chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# #打开网页
# driver.get("https://www.baidu.com")
# print(driver.title)

# 隐藏正在受到自动化测试软件的控制这句话
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',
                                       ['enable-automation'])

service = Service("../../chromedriver.exe")
driver = webdriver.Chrome(service=service,options=chrome_options)
#
# # 把浏览器最大化
# driver.maximize_window()
# # 使用id进行定位
# input_element = driver.find_element(by=By.ID,value="kw")
# # 往输入框中输入内容
# input_element.send_keys("大周老师")
# search_button = driver.find_element(by=By.ID,value="su")
# # 点击搜索按钮
# search_button.click()

#打开网页
driver.get("https://www.jd.com")
print(driver.title)
 # 把浏览器最大化
driver.maximize_window()
# jd_search_input = driver.find_element(by=By.CLASS_NAME,value="text")
# jd_search_input.send_keys("电脑")
# jd_search_button = driver.find_element(by=By.CLASS_NAME,value="button")
# jd_search_button.click()
# link_text指的是链接上面的文字
driver.find_element(by=By.LINK_TEXT,value="家用电器").click()


# 当页面以一个新的页面打开时，将会出现多个句柄（就是浏览器的页面），需要切换切换操作句柄
# 句柄切换
# 1.拿到所有句柄
handlers = driver.window_handles
# 2.迭代当前句柄
for h in handlers:
    # 如果h不等于当前的handlers
    if h!= driver.current_window_handle:
#         切换到这个句柄上
        driver.switch_to.window(h)
    print("当前句柄是："+driver.title)


# partial_link_text指的是链接上的部分文字
driver.find_element(by=By.PARTIAL_LINK_TEXT,value="一体").click()
