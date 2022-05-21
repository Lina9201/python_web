from selenium import webdriver

# selenium 会到指定路径将chromedriver服务启动起来，开启与浏览器之间的会话
driver = webdriver.Chrome('C:\software\Python\chromedriver.exe')

driver.get('https://www.baidu.com/')

print(driver.title)

# 窗口最大化
driver.maximize_window()

driver.get('https://www.taobao.com')

# 回退到上一页
driver.back()

# 回到下一页
driver.forward()

# 刷新
driver.refresh()

# 获取网址
print(driver.current_url)

# 获取窗口句柄
print(driver.current_window_handle)

driver.quit()