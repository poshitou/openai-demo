import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
os.environ["OPENAI_API_KEY"] = "sk-3uQYgvt4coIjaPxM2ZrWAdMFrsQY4Ftaxir9Xyc9GvIsTrsf"
os.environ["OPENAI_API_BASE"] = "https://api.fe8.cn/v1"

# os.environ["OPENAI_API_KEY"] = "sk-WHRCoUdd39GWq4RW084f16CeBaAc4f21BdD178F6Ba55Fd80"
# os.environ["OPENAI_API_BASE"] = "https://api.xty.app/v1"
# 设置 Chrome 无头模式
chrome_options = Options()
chrome_options.add_argument("--headless")  # 开启无头模式
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 启动 Chrome 浏览器
driver = webdriver.Chrome(options=chrome_options)

try:
    # 打开 Google 首页
    driver.get("https://www.google.com")

    # 查找搜索框并输入关键词“养生”
    search_box = driver.find_element("name", "q")
    search_box.send_keys("养生")
    search_box.send_keys(Keys.RETURN)  # 执行搜索

    # 等待搜索结果加载
    driver.implicitly_wait(10)  # 等待最多 10 秒

    # 打印页面标题
    print(driver.title)

finally:
    # 关闭浏览器
    driver.quit()
