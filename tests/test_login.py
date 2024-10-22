import unittest
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 自动管理 ChromeDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--ignore-certificate-errors')  # 跳过 SSL 验证
        options.add_argument('--allow-insecure-localhost')  # 允许不安全的本地主机
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--allow-http-screen-capture')
        # 不使用无头模式
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    
    def test_1_login_with_invalid_data(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com")

        # 读取数据文件
        with open('tests/data/invalidData.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        email = lines[0].strip()
        password = lines[1].strip()

        # 使用显式等待，直到 "SIGN UP NOW!" 元素可见
        try:

            # 等待页面跳转并确认当前 URL
            # WebDriverWait(self.driver, 10).until(
            #     EC.url_changes("https://www.wizmarketplace.com/signup")
            # )

            # 检查当前 URL 是否为目标 URL
            # self.assertIn("expected_url_part", self.driver.current_url, "未跳转到预期的 URL")

             # 验证并点击 "Sign up with email" 按钮
           
            # 使用 XPath 定位包含特定文本的元素
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Do not display again')]"))
            )
    
            # 点击元素
            button.click()

            # time.sleep(3)  # 等待 5 秒以确保页面加载
             # 等待并找到按钮
            # profile_button = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//a[@href='/user/my-profile']"))  # 根据 href 查找链接
            # )

            # # # 点击按钮
            # profile_button.click()
            # 使用 XPath 定位 alt 属性为空的 <img> 元素
            # 使用 WebDriverWait 等待 class 包含 'jss90' 的 <img> 元素变得可点击
            # 使用 WebDriverWait 等待 href 属性以 "/aa/dd" 开头的 <a> 元素变得可见
            # link_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//a[starts-with(@href, '/user/my-profile')]"))
            # )
            link_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[starts-with(@href, '/user/my-profile')]"))
)
            print("2222:",link_element)
            # 可以执行其他操作，例如获取 href 属性的值
            href_value = link_element.get_attribute('href')

            print("111111111",href_value)

            # self.driver.execute_script("arguments[0].scrollIntoView(true);", link_element)

            # self.driver.execute_script("arguments[0].click();", link_element)
            # 直接使用 WebDriver 跳转到该 URL
            self.driver.get("https://www.wizmarketplace.com/login")
    
            # 如果你想点击这个链接
            # link_element.click()


            # time.sleep(3)  # 等待 5 秒以确保页面加载


            # email_button = WebDriverWait(self.driver, 3).until(
            #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign up with email')]"))
            # )
            # print("000000000000",email_button.is_enabled())
            # self.assertTrue(email_button.is_displayed(), "Sign up with email 按钮未显示")  # 验证按钮是否可见
            # email_button.click()  # 点击按钮
             # 使用 JavaScript 点击按钮
            # self.driver.execute_script("arguments[0].click();", email_button)

            # time.sleep(5)  # 等待 5 秒以确保页面加载

            # # # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


            # # # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
            )
    
            # 点击按钮
            login_button.click()

            time.sleep(3)


            # 使用 WebDriverWait 等待 "Invalid email" 文本变得可见
            invalid_email_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Invalid email')]"))
            )
    
            # 断言 "Invalid email" 文本确实存在
            assert "Invalid email" in invalid_email_element.text, "页面上不存在 'Invalid email' 元素"
          


            # myFavourites_element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//a[starts-with(@href, '/user/my-favourites')]"))
            # )

            # 点击my myFavourites_element
            # myFavourites_element.click()

            # self.driver.get(href_value)

            # 使用 WebDriverWait 等待 <input> 元素变得可见
            # email_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.ID, ":r3:"))
            # )
    
            # 获取 <input> 元素的 value 属性
            # email_value = email_element.get_attribute('value')
    
            # # 断言 value 属性是否为 "meng.li.aroma@gmail.com"
            # assert email_value == "meng.li.aroma@gmail.com", "login failed"



        except Exception as e:
            self.fail(f"测试失败: {e}")
    
    def test_2_login_with_valid_data(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/login")

        # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        email = lines[0].strip()
        password = lines[1].strip()

        # 使用显式等待，直到 "SIGN UP NOW!" 元素可见
        try:
            # # # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


            # # # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
            )
    
            # 点击按钮
            login_button.click()

            time.sleep(5)

            # 获取所有cookie
            cookies = self.driver.get_cookies()
            print("cookies after login is:",cookies)

            # 遍历cookie列表以查找token
            # 打印所有cookie信息
            token = None
            for cookie in cookies:
                if cookie['name'] == 'token':  # 假设token存储在名为'access_token'的cookie中
                    token = cookie['value']
                    print("token in cookies is:",token)
                    break

            # 打印获取到的token
            print("Token:", token)

            # 断言token不为None
            assert token is not None, "Token is None"

            return token


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_7_profile_change_password(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/user/my-profile")

        # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

        current_password = lines[1].strip()


        try:    

            changePassword_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()='Change password']"))
            )
            assert changePassword_link is not None, "找不到 Change password 链接"

            changePassword_link.click()


            current_password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "password"))
            )

            current_password_input.send_keys(current_password)

            # 使用 By.NAME 选择器来定位元素
            new_password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "newPassword"))
            )
        
            # 断言元素存在
            assert new_password_input is not None, "新密码输入框不存在"

            new_password_input.send_keys("Test123456")


            confirm_password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "confirmPassword"))
            )

            confirm_password_input.send_keys("Test123456")

            save_changes_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE CHANGES']"))
            )
    
            # 点击按钮
            save_changes_button.click()

            time.sleep(1)

            # 使用 WebDriverWait 等待元素变得可见
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
    
            # 获取元素的文本内容
            message_text = success_message.text.strip()

            # 断言元素存在，并且文案是 "Password has been updated successfully"
            assert success_message is not None, "成功提示元素不存在"
            assert message_text == "Password has been updated successfully", "成功提示文案不符合预期"
        
        
        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_8_login_with_new_password(self):

         # 模拟随机延迟
        # 刷新当前页面
        time.sleep(10)     

        # logout_link = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//p[text()='Log out']"))  # 根据 ID 查找输入框
        # )

        # logout_link = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//p[text()='Log out']"))
        # )

        # print("logout_link is: ",logout_link)



        # logout_link.click()

        # 使用 WebDriverWait 等待 "Log out" 文本变得可见
        logout_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Log out')]"))
        )
    
        # 点击 "Log out" 元素
        logout_element.click()


        logout_page = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='You’re now logged out!']"))  # 根据 ID 查找输入框
        )

        
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/login")

        # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        email = lines[0].strip()
        password = "Test123456"

        # 使用显式等待，直到 "SIGN UP NOW!" 元素可见
        try:
            # # # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


            # # # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
            )
    
            # 点击按钮
            login_button.click()

            time.sleep(5)

            # 获取所有cookie
            cookies = self.driver.get_cookies()
            # print("cookies after login is:",cookies)

            # 遍历cookie列表以查找token
            # 打印所有cookie信息
            token = None
            for cookie in cookies:
                if cookie['name'] == 'token':  # 假设token存储在名为'access_token'的cookie中
                    token = cookie['value']
                    print("token in cookies is:",token)
                    break

            # 打印获取到的token
            # print("Token:", token)

            # 断言token不为None
            assert token is not None, "Token is None"

            return token


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_3_filter_product_by_featured(self):
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒

        self.driver.get("https://www.wizmarketplace.com/listing")
        # time.sleep(random.uniform(3, 5))  # 随机延迟 1 到 3 秒


        try:


            
            featured_filter_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Featured')]"))
            )

            featured_filter_button.click()

            self.driver.refresh()

            # 使用 WebDriverWait 等待含有特定 href 属性的元素变得可见
            # target_element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/daisy-bean-bag-i.1679756265905917953']"))
            # )

            # element_xpath = "//a[@href='/product/daisy-bean-bag-i.1679756265905917953']"

            # # 滚动到元素可见
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, element_xpath))

            # # 等待元素可见
            # target_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, element_xpath))
            # )

            element_xpath = "//a[contains(@href, '1679756265905917953')]"

            # 滚动到页面底部，以便加载可能处于视图之外的元素
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 等待元素可见
            product_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))
            )

            print("target_element is:",product_link)

            assert product_link is not None, "找不到featured的产品"
    
            # 点击该元素
            product_link.click()

            add_to_cart_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )

            assert add_to_cart_element is not None, "Add to cart button does not exist"

            # color_element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@style, 'background-color: rgb(0, 188, 0);')]"))
            # )

            # element_with_style = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//button[contains(@style, 'background-color: rgb(0, 188, 0)')]"))
            # )

            # 使用 WebDriverWait 等待第一个匹配的元素变得可见
            # first_button = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeMedium"))
            # )
            # 构建XPath表达式，匹配具有特定style属性的元素
            style_attribute = "background-color: rgb(239, 223, 202); border: 0.5px solid transparent;"
            locator = (By.XPATH, f"//div[contains(@style, '{style_attribute}')]")

            # 使用WebDriverWait和EC.visibility_of_element_located来等待元素可见
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.click()
            

            add_to_cart_element.click()

            time.sleep(1)

            successful_tip = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
            assert successful_tip is not None, "add to cart fail"

            # 获取 error tips 元素的文本内容
            successful_text = successful_tip.text
            assert "Added to cart successfully" in successful_text, "add to cart fail"

        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_4_view_cart(self):
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒'
        # self.driver.get("https://www.wizmarketplace.com/cart")
        try:
            # 获取右上角的购物车图标
            view_cart_locator = (By.XPATH, '//*[@data-testid="ShoppingCartIcon"]')

            # 点击购物车图标，打开购物车侧边栏
            view_cart_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(view_cart_locator))
            view_cart_element.click()


            time.sleep(3)
            # 点击View Cart按钮
            view_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View Cart')]"))
            )

            view_cart_button.click()

            time.sleep(3)

            # 增加数量
            # add_icon_locator = '//*[@data-testid="AddIcon"]'

            # 滚动到元素可见
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, add_icon_locator))

            # 等待元素可见
            # add_icon_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, add_icon_locator))
            # )

            # assert add_icon_element is not None, "没能来到购物车页面"
            # add_icon_element.click()

            # time.sleep(3)



            # 验证数量为2
            quantity_locator = (By.XPATH, "//p[text()='1']")
            quantity_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(quantity_locator))

            assert quantity_element is not None, "个数不是2"

        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_5_checkout(self):

        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/cart")
        
        try:

            # time.sleep(20)
            # 定义CSS选择器，匹配按钮文本
            # checkout_locator = 

            # 使用WebDriverWait等待元素可见并点击
            # checkout_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(checkout_locator))
            
            time.sleep(3)
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//button[@type="button"]'))
            )

            checkout_button.click()

            # time.sleep(3)

            # locator = (By.CSS_SELECTOR, "p:contains('Customer Information')")
            
            # assert locator is not None, "dfdf"

            customer_information_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Customer Information')]"))
            )

            assert customer_information_text is not None,"dfsfsdf"

            change_delivery_address_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'primary') and contains(text(), 'Change')]"))
            )

            change_delivery_address_button.click()

            time.sleep(3)

            # add_new_address_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Add New Address')]"))
            # )

            # 定位到元素的 XPath
            element_xpath = "//p[contains(text(), 'Add New Address')]"

            # 滚动到元素可见
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, element_xpath))

            # 等待元素可见
            add_new_address_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))
            )

            add_new_address_element.click()

            # # # 验证firstName是否存在
            Name_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":ro:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            Name_input.send_keys("Aroma1")


            # # # 验证firstName是否存在
            phone_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":rp:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            phone_input.send_keys("00000000000")


            # # # 验证firstName是否存在
            street_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":rq:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            street_input.send_keys("my address")


            # # # 验证firstName是否存在
            code_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":rr:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            code_input.send_keys("100087")


            # default_checkbox = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, '//input[@ype="checkbox")]'))
            # )

            # 使用XPath定位类型为checkbox的<input>元素
            # default_checkbox_locator = (By.XPATH, "//input[@type='checkbox']")

            # 使用WebDriverWait等待元素可见
            # default_checkbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))

            # default_checkbox = (By.XPATH, '//*[@data-testid="CheckBoxOutlineBlankIcon"]')


            # default_checkbox.click()

            # default_checkbox.click()


            save_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'primary') and contains(text(), 'Save')]"))
            )

            save_button.click()

            time.sleep(1)

            successful_tip = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
            assert successful_tip is not None, "add to cart fail"

            # 获取 error tips 元素的文本内容
            successful_text = successful_tip.text
            assert "New delivery address added" in successful_text, "添加地址不成功"

            # time.sleep(3)

            # confirm_button = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'primary') and contains(text(), 'Confirm')]"))
            # )

            # confirm_button.click()


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_6_clear_cart(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/cart")

        try:
            delete_selected_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Delete Selected')]"))
            )
            delete_selected_element.click()

            empty_text_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Your cart is empty.')]"))
            )

            assert empty_text_element is not None, "购物车不为空"
            
        except Exception as e:
            self.fail(f"测试失败: {e}")


    def test_9_change_password_back(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/user/my-profile")

        # # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

        new_password = lines[1].strip()

        # # 读取数据文件
        
        changePassword_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Change password']"))
        )
        assert changePassword_link is not None, "找不到 Change password 链接"

        changePassword_link.click()


        current_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )

        current_password_input.send_keys("Test123456")

        # # 使用 By.NAME 选择器来定位元素
        new_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "newPassword"))
        )
        
        # # 断言元素存在
        assert new_password_input is not None, "新密码输入框不存在"

        new_password_input.send_keys(new_password)


        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "confirmPassword"))
        )

        confirm_password_input.send_keys(new_password)

        save_changes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE CHANGES']"))
        )
    
        # # 点击按钮
        save_changes_button.click()

        time.sleep(1)

        # # 使用 WebDriverWait 等待元素变得可见
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
        )
    
        # # 获取元素的文本内容
        message_text = success_message.text.strip()

        # # 断言元素存在，并且文案是 "Password has been updated successfully"
        assert success_message is not None, "成功提示元素不存在"
        assert message_text == "Password has been updated successfully", "成功提示文案不符合预期"

        
             


    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        
        

if __name__ == "__main__":
    unittest.main()
