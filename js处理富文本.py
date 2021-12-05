from selenium import webdriver
import time

class Test1:

    def login(self):
        # 个人资料路径
        user_data_dir = r'--user-data-dir=C:\Users\ZXFW\AppData\Local\Google\Chrome\User Data'
        # 加载配置数据
        option = webdriver.ChromeOptions()
        option.add_argument(user_data_dir)
        driver = webdriver.Chrome(chrome_options=option, executable_path=r'C:\software\Python\chromedriver.exe')
        # 账号密码UI登录方式
        # blogurl = "https://account.cnblogs.com/signin"
        # driver.get(blogurl)
        # login_account = driver.find_element_by_xpath("//input[@placeholder='登录用户名 / 邮箱']")
        # login_account.clear()
        # login_account.send_keys('feifei妹纸')
        # login_password = driver.find_element_by_xpath("//input[@placeholder='密码']")
        # login_password.clear()
        # login_password.send_keys('zxfw779616131')
        # login_button = driver.find_element_by_xpath("//span[text()=' 登录 ']")
        # login_button.click()
        # time.sleep(3)
        # print(driver.get_cookies())

        # cookie登录方式
        # cookie = {
        #     'domain': 'account.cnblogs.com',
        #     'expiry': 1638713571,
        #     'httpOnly': False,
        #     'name': '4271c12252a544478175bac9772afc3d',
        #     'path': '/',
        #     'secure': False,
        #     'value': '15be0c3f-66fb-4e6c-8f50-c3c9492b1c7d'
        # }
        # self.driver.add_cookie(self.driver.get_cookies()[0])

        driver.get("https://www.cnblogs.com/Lina-zhu/")
        time.sleep(4)


if __name__ == "__main__":
    Test1().login()
