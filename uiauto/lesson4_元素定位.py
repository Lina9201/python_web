from selenium import webdriver

# selenium 会到指定路径将chromedriver服务启动起来，开启与浏览器之间的会话
driver = webdriver.Chrome('C:\software\Python\chromedriver.exe')

driver.get('https://www.baidu.com/')

ele = driver.find_element_by_id('kw')
print(ele.get_attribute('class'))

# 返回所有元素
eles = driver.find_elements_by_class_name('s_ipt')
# 出现符合条件的第一个元素
driver.find_elements_by_class_name('s_ipt')

driver.find_element_by_name('wd')

driver.find_element_by_tag_name('input')

# 针对链接
driver.find_element_by_link_text("更多产品")
driver.find_elements_by_partial_link_text("产品")

driver.quit()